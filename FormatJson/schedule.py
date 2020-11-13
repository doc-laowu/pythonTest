#-*- coding: UTF-8 -*-
# ==================================================================================================
# desc          : 数据中心spark计算程序的调度器，通过定时查询源数据库中的数据获取活动id来启动计算作业
# created info  : system 2020-04-27 11:40:15
# note          : yisheng.wu
# ==================================================================================================
import datetime
import pymysql
from pymysql.cursors import DictCursor
import logging
import logging.handlers
import os
import time

# 封装的日志的类文件
class logs(object):
    def __init__(self):
        self.logger = logging.getLogger("")
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        # 创建文件目录
        logs_dir = "/vhallapp/logs"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = 'schedule-%s.log' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

# 日志对象
logger = logs()

# 调度用户中心计算程序的类
class schedule:
    # 全局的连接对象
    connection = None
    cursor = None

    def __init__(self):
        RDS_SOURCE_HOST = "am-2ze85jk72mn38c261131910.ads.aliyuncs.com"
        RDS_SOURCE_USERNAME = "ads_test_root"
        RDS_SOURCE_PASSWORD = "ads_test_root@vhall2020"
        RDS_SOURCE_DB = "activity_support_service"

        # 连接数据库
        try:
            self.connection = pymysql.connect(
                host=RDS_SOURCE_HOST,
                port=3306,
                user=RDS_SOURCE_USERNAME,
                passwd=RDS_SOURCE_PASSWORD,
                db=RDS_SOURCE_DB,
                cursorclass=DictCursor,
                charset='utf8'
            )

            self.cursor = self.connection.cursor()
        except Exception:
            logger.error("connect to the ads occur error, [ %s ]" % (Exception))

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    """
        获取要执行的活动id
    """
    def getBusinessUid(self, yesterday):

        sql = """SELECT 
                DISTINCT A.business_uid
                FROM 
                b_is_compute AS BIC
                INNER JOIN 
                (
                    SELECT
                    UBL.business_uid, UBL.bu
                    FROM user_behavior_log AS UBL INNER JOIN activity_live AS AL
                    ON UBL.business_uid = AL.business_uid AND UBL.activity_id = AL.activity_id AND UBL.bu = AL.bu 
                    WHERE DATE(UBL.occur_time) = %s AND UBL.behavior = 6
                ) AS A 
                ON A.business_uid = BIC.business_uid AND A.bu = BIC.bu 
                WHERE BIC.is_compute = 1
            """
        try:
            self.cursor.execute(sql, yesterday)
            results = self.cursor.fetchall()
            if(len(results) > 0):
                logger.warning("the yestoday time is [ %s ], sleect from database activity_id is [ %s ]" % (yesterday, results))
            else:
                logger.warning("the yestoday time is [ %s ], sleect from database activity_id is [ None ]" % (yesterday))
        except Exception:
                    logger.error("select activity_id occur error, the root cause is [ %s ]" % (Exception))

        return results

    """
        调用shell脚本
    """
    def invokShell(self, path, business_uids):
        logger.warning("schedule business_uids is [ %s ] to submit user_calculate_service's path is [ %s ]" % (business_uids, path))
        try:
            os.system('/bin/sh %s %s' % (path, business_uids))
        except Exception as e:
            logger.error("Invoke the shell script error, [ %s ]" % e)

    """
        提交job任务
    """
    @staticmethod
    def submitJob(yesterday, path, service_names):
        # 提交的活动数
        BatchSize = 10

        scheduleRef = schedule()

        businessUids = scheduleRef.getBusinessUid(yesterday)

        index = 0
        businessUidStr = str()
        for business_uid in businessUids:
            index += 1
            if(index % BatchSize == 0):
                # 调用执行命令
                businessUidStr = businessUidStr + str(business_uid["business_uid"]) + ","
                businessUidStr = businessUidStr[0:len(businessUidStr)-1]
                scheduleRef.invokShell(path, businessUidStr)
                businessUidStr = str()
                # 每30s提交一个任务
                time.sleep(30)
            else:
                businessUidStr = businessUidStr+str(business_uid["business_uid"])+","

        if(index != 0 and (index % BatchSize) != 0):
            businessUidStr = businessUidStr[0:len(businessUidStr) - 1]
            scheduleRef.invokShell(path, businessUidStr)


if(__name__ == "__main__"):

    shellPath = "/vhallapp/real_warehouse/user_calculate_service/run.sh"

    # 获取昨天的时间
    yesterday = datetime.date.today() + datetime.timedelta(-1)

    # 查询活动id并提交任务
    schedule.submitJob(yesterday, shellPath, 0)