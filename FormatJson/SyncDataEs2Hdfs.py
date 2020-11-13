#-*- coding: UTF-8 -*-
# ==================================================================================================
# desc          : 从elasticsearch同步数据到hdfs上的py脚本
# created info  : system 2020-07-14 14:57:15
# note          : yisheng.wu
# ==================================================================================================

import datetime
import time
import json
import os
import sys
from elasticsearch import Elasticsearch

def local2utc(time_str):
    """给定时间转UTC时间(-8:00)字符串
    """
    time_s = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time_struct = time.mktime(time_s)
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    utc_time_str = utc_st.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return utc_time_str

if __name__ == "__main__":

    # -----------------------------------------------------------------
    #            执行从elasticsearch中查询数据写入到日志文件中
    # -----------------------------------------------------------------

    yestoday = None
    dt = None

    # 获取外部参数
    if(len(sys.argv)-1 > 0):
        yestodayDate = datetime.datetime.strptime(sys.argv[0], "%Y%m%d")
        dt = sys.argv[1]
        yestoday = local2utc(yestodayDate.strftime('%Y-%m-%d 00:00:00'))
        today = local2utc((yestodayDate + datetime.timedelta(1)).strftime('%Y-%m-%d 00:00:00'))
    else:
        yestodayDate = datetime.date.today() + datetime.timedelta(-1)
        dt = yestodayDate.strftime('%Y%m%d')
        yestoday = local2utc(yestodayDate.strftime('%Y-%m-%d 00:00:00'))
        today = local2utc(datetime.date.today().strftime('%Y-%m-%d 00:00:00'))

    ip = ['192.168.13.32']
    http_auth = ()
    # 获取elasticsearch的type名字
    index = "srs_report_stat-*"
    type = "srs_report_stat-" + dt

    filepath = "/vhallapp/logs/"+type+".log"

    # 初始化连接elasticsearch
    elasticsearch = Elasticsearch(hosts=ip, port=9200)

    # 判断文件是否存在
    fd = None
    if(os.path.isfile(filepath)):
        os.remove(filepath)
    fd = open(file=filepath, mode='a+')

    # 查询数据的总条数
    dsl = {
        "query":{
            "range":{
                "@timestamp":{
                    "gte": "%s" % yestoday,
                    "lt": "%s" % today
                }
            }
        }
    }

    queryData = elasticsearch.search(index=index, scroll='20m', timeout='30s', size=1000, body=dsl)
    total = queryData["hits"]["total"]
    if(total > 0):
        scroll_id = queryData["_scroll_id"]
        total = queryData["hits"]["total"]

        # 写入文件
        mdata = queryData.get("hits").get("hits")
        for item in mdata:
            fd.write(json.dumps(item['_source']))
            fd.write('\n')

        while True:
            res = elasticsearch.scroll(scroll_id=scroll_id, scroll='5m')
            mdata = res["hits"]["hits"]
            if(len(mdata) <= 0):
                break
            for item in mdata:
                fd.write(json.dumps(item['_source']))
                fd.write('\n')
    # 关闭文件
    fd.flush()
    fd.close()
    # 关闭elasticsearch的链接
    elasticsearch.close()

    # -----------------------------------------------------------------
    #                       执行将日志文件导入到Hive表中
    # -----------------------------------------------------------------
    hiveTable  = "ods.ods_live_log_di"
    hiveTablePath = "/user/hive/warehouse/ods.db/ods_live_log_di/dt=%s" % dt
    load2hive= """
        /usr/local/hive2.1/bin/hive -e \"alter table %s add if not exists partition(dt=%s) location \'%s\';
        load data local inpath \'%s\' into table %s partition(dt=%s);\"
    """ % (hiveTable, dt, hiveTablePath, filepath, hiveTable, dt)
    os.system(load2hive)
