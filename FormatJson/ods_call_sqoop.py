# #-*- coding: UTF-8 -*-
# # ==================================================================================================
# # desc          : 从elasticsearch同步数据到hdfs上的py脚本
# # created info  : system 2020-07-14 14:57:15
# # note          : yisheng.wu
# # ==================================================================================================
# import logging
# import logging.handlers
# import os
# import time
#
# filename='/home/message/data.txt'
# filename='C:\\Users\\gaosen\\Documents\\WeChat Files\\wxid_td6365q1dllc22\\FileStorage\\File\\2020-08\\20200816数据导出.csv'
# sqoop_filename='/home/message/ods_message.sh'
# target_file = "E:\\ods_message_data.txt"
#
# index=0
# channel=""
# BATCH_SIZE=10
#
# wf = open(target_file, 'a')
#
# for line in open(filename, encoding= 'utf-8'):
#     channel_id=line.split(",")[0].strip('\"')
#     channel=channel+",'"+channel_id+"'"
#     index=index+1
#     if(index % BATCH_SIZE == 0):
#         cmd = "bash %s '%s'" % (sqoop_filename, channel)
#         wf.write(channel+"\n")
#         channel=""
#
# if(index % BATCH_SIZE != 0 and index > 0):
#     wf.write(channel + "\n")
#
# wf.flush()
# wf.close()
import datetime

# lastDate= {}
#
# end_time = "2020-%s-%s %s:00" % ("09", "09", "23:59")
# end_time=(datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(-1)).strftime("%Y-%m-%d %H:%M:%S")
# lastDate['lastDate'] = end_time
# print(lastDate)


my_dict = {"name":"123213", "asdasd":1231}
if(not bool(my_dict)):
    print("Dictionary is empty")
elif(bool(my_dict)):
    print("Dictionary is not empty")


arr = ['asdasd']
str = ','.join(arr)
print(str)















