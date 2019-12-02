#-*- coding: UTF-8 -*-
import datetime
import json
import sys
import os
import requests
import io
import time

# 加载参数
if(len(sys.argv) == 4):
    business_uid = sys.argv[1]
    group_id = sys.argv[2]
    file_path = sys.argv[3]
    cur_date = sys.argv[4]
else:
    business_uid = 5300001
    group_id = 23800002
    file_path = "C:\\Users\\gaosen\\Desktop\\data.file"
    cur_date = (datetime.date.today() + datetime.timedelta(-1)).strftime("%Y%m%d")

# 导数据的url
url="http://test-api-bc.vhall.domain/consumer/user-import"
#
# # 将数据导出到本地中
# HQL='''SELECT
#     nick_name,
#     phone,
#     email
#     FROM
#     app.fact_saas_user_no_payed
#     WHERE
#     dt = %s;''' % cur_date
#
# # 将数据导出到本地机器中
# os.system('''/usr/local/hive2.1/bin/hive -S -e "%s" > %s''' % (HQL, file_path))
#
# # 将数据文本中的第一行表头去掉
# os.system("sed -i '1d' %s" % file_path)

# 初始化data数组
data = []

# 请求的格式头
body = {
    "business_uid": business_uid,
    "group_id": group_id,
    "data": data,
    "bu": '0'
}

# 打开文件
f = io.open(file_path, 'r', encoding='UTF-8')

# 读取文件
lines = f.readlines()
# 文件索引行数
index = 0
# 多少条数据请求一次
gap = 500
# 文件行数
length = len(lines)

for line in lines:

    index = index + 1

    str_arr = line.strip('\n').split("\t")

    # 拼接json数据体
    json_dict = {
        "phone": str_arr[1],
        "real_name": str_arr[0],
        "sex": "",
        "email": str_arr[2],
        "industry": "",
        "position": "",
        "birthday": "",
        "education_level": "",
        "remark": ""
    }
    data.append(json_dict)
    body['data'] = json.dumps(data)

    # 当有500条时，进行get请求
    if(index % gap == 0 or length == index):
        response = requests.post(url, data=body)
        print("index: %s" % index)
        print("status: %s" % response.status_code)
        print("content: %s " % json.loads(response.text))
        # print("body: %s " % json.dumps(body))
        print("-------------------------------------------")
        data.clear()
        time.sleep(3)

f.close()