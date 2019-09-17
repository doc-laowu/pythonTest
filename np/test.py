# coding=utf-8
import os
import re
import sys
import time
import httplib
import urlparse
import argparse
import base64
import json

# 顺序不能变，要与文档一一对应
browser_list = [
    {"qqbrowser": "QQBrowser"},
    {"micromessenger": "MicroMessenger"},
    {"ucbrowser": "UCBrowser"},
    {"lbbrowser": "LieBaoBrowser"},
    {"maxthon": "Maxthon"},
    {"se2.x": "SogouBrowser"},
    {"360se": "360Browser"},
    {"360chrome": "360Browser"},
    {"firefox": "FireFox"},
    {"chrome": "Chrome"},
    {"opera": "Opera"},
    {"msie": "IE"},
    {"safari": "Safari"},
    {"omniweb": "OmniWeb"},
    {"netscape": "Netscape"},
    {"netcaptor": "NetCaptor"},
    {"lynx": "Lynx"}
]


# 获取浏览器类型，返回对应code
def get_browser(log_line):
    ip = r"?P<ip>[\d.]*"
    date = r"?P<date>\d+"
    month = r"?P<month>\d+"
    year = r"?P<year>\d+"
    log_time = r"?P<time>\S+"
    method = r"?P<method>\S+"
    request = r"?P<request>\S+"
    status = r"?P<status>\d+"
    body_bytes_sent = r"?P<bodyBytesSent>\d+"
    refer = r"""?P<refer>
             [^\"]*
             """
    user_agent = r"""?P<userAgent>
                .*
               """
    p = re.compile(
        r"(%s)\ -\ -\ \[(%s)-(%s)-(%s)T(%s) [\S]+\]\ \"(%s)?[\s]?(%s)?.*?\"\ (%s)\ (%s)\ \"(%s)\"\ \"(%s).*?\"" %
        (ip, year, month, date, log_time, method, request, status, body_bytes_sent, refer, user_agent), re.VERBOSE)


    # 提取了日志的所有信息，目前只使用user_agent。
    m_list = re.findall(p, log_line)
    if len(m_list) == 0:
        return "Other"

    m_set = m_list[0]
    if len(m_set) != 11:
        return "Other"

    original_browser = m_set[10].lower()

    print(m_set[10])

    if not original_browser:
        return "Other"

    for browser in browser_list:
        if browser.keys()[0] in original_browser:
            print(original_browser)
            return browser.values()[0]
    return "Other"


# f = open("C:\\Users\\gaosen\\Documents\\Tencent Files\\924602208\\FileRecv\\log\\test_access.log")
# for line in f:
#     print(get_browser(line.strip()))
# f.close()

# str = """eyJzIjoiZjdiNWRlYjJlZmQ0MmRmZjdlMTI2NWE2NjIzMTEyNmIiLCJidSI6MSwiYWlkIjoiaW5hdl8yMTEyMzJmNCIsInBmIjo1LCJ1aWQiOiJiNmQ2ZjIxYV9CS0wtQUwwMCIsInZpZCI6Ijc0NiIsInZmaWQiOiI3NDYiLCJhcHBfaWQiOiJiNmQ2ZjIxYSIsIm5kaSI6Ijg2Njk1NDAzMjQxOTgyMyIsImlwIjoiMS4xMTkuMTkzLjM2IiwiZ3VpZCI6IkJLTC1BTDAwIiwiYWNjb3VudF9pZCI6Ijc0NiIsImFwcF9uYW1lIjoi5L2g5Li25Li25Li25Y+j5rC05pyJ5q+SIiwidnR5cGUiOjIsInZlciI6IjIuMS4xLjEiLCJkYXRlIjoiMjAxOTAyMjYiLCJwIjoiMjA0NTczNTQ0MDc5Mzc5NDAwIiwidGYiOjY2MjcwMywidmlkZW9IZWlnaHQiOiIxODAiLCJ2aWRlb1dpZHRoIjoiMjQwIiwib3MiOmZhbHNlLCJiaXRyYXRlIjoxNzYsInR0IjozMDAwM30="""
# print(base64.decodestring(str))


# map = {"age":24, "name":"cool_summer_moon", "id":"", "xx":None, "asd":None}
#
# print(json.dumps(map))

log = '''1.119.193.36 - - [2019-03-29T15:35:19+08:00] "GET /login?k=92005&id=1553844920654&s=7382115538448137863&bu=2&token=eyJzIjoiNzM4MjExNTUzODQ0ODEzNzg2MyIsInAiOiJlZHVfMjQ3M2UzYmFfbGl2ZSIsInVpZCI6IjczODIxIiwiYWlkIjoiZWR1XzI0NzNlM2JhX2xpdmUiLCJwZiI6MywidmlkIjoiMTI1IiwidmZpZCI6IjEyNSIsIm5kaSI6IiIsImd1aWQiOiIiLCJ2dHlwZSI6IiIsInRvcGljIjoiIiwiZmQiOiJ2aGFsbGNsYXNzL3ZoYWxscmVjb3JkL2VkdV8yNDczZTNiYV9saXZlLzIwMTkwMzExMTcwNDA1XzY5MDMvcmVjb3JkLm0zdTgiLCJ0dCI6Mjk4MDEuNjczOTk5OTk5OTg1LCJiYyI6MSwiYnQiOjIsInNkIjoiaHR0cHM6Ly90LWN5aGxzdm9kaGxzMDIudmhhbGx5dW4iLCJhcHBfaWQiOiIiLCJmcm9tIjoiIiwidGYiOjAsImJpel9yb2xlIjoyLCJmbG93X3R5cGUiOjIsImJpel9pZCI6ImVkdV8yNDczZTNiYSIsImJpel9kZXMwMSI6IjEifQ== HTTP/1.1" 200 3 "https://t-m-class.e.vhall.com/" "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11s Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044604 Mobile Safari/537.36 V1_AND_SQ_7.9.9_1010_YYB_D QQ/7.9.9.3965 NetType/WIFI WebP/0.3.0 Pixel/1080 StatusBarHeight/54" "-"'''

# print(get_browser(log.strip()))

info = '''陈先生
电话：15012474477
手机：18928433990

梁先生
手机：18682018724

苏先生
手机：13925052099'''

strArr = info.split("\n\n")

tel = ""
name = ""
phone = ""

for str in strArr :
    strArr2 = str.split("\n")
    for str2 in strArr2 :
        if str2.__contains__("电话："):
            tel = str2.split("电话：")[1]
        elif str2.__contains__("手机："):
            phone = str2.split("手机：")[1]
        else:
            name = str2

    print("name:" + name + ", tel:" + tel + ", phone:" + phone + "\n")
    name,tel,phone = "", "", ""

























