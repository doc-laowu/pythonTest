#-*- coding: UTF-8 -*-
import json
import random
from queue import Empty

import time
from pykafka import KafkaClient

client = KafkaClient(hosts="*")
topic = client.topics['test_sink_new_client_ods_latest']

producer = topic.get_producer(delivery_reports=True)

ip = ['*']

count = 0
for i in range(1000):
    count += 1

    src_ip = ip[random.randint(0, 4)]

    nginx_utc_datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    data = {
        "tt": "30000",
        "code": "182004",
        "mod": "18",
        "vtype": "2",
        "bitrate": "646",
        "type": "2",
        "process_time": "2020-08-04 10:43:31",
        "videoHeight": "477",
        "videoWidth": "848",
        "src_ip": src_ip,
        "uid": "15033544320",
        "uf": "2387304",
        "sd": "172.16.11.110:443",
        "bu": "0",
        "tag": "login",
        "app_id": "1008611",
        "errorcode": "2003",
        "ver": "1.2.5",
        "biz_role": "",
        "os": "false",
        "log_session": "13281423836",
        "_m": "",
        "p": "847619034251956600",
        "browser_name": "Chrome",
        "tf": "37430",
        "s": "13281423836",
        "biz_des01": "",
        "pf": "7",
        "biz_des02": "1",
        "nginx_utc_datetime": nginx_utc_datetime,
        "biz_id": "",
        "aid": "lss_9527nmsl",
        "biz_id":"9527dream"
    }
    josn_str = json.dumps(data)

    print("cur_date:" + nginx_utc_datetime + "; data:" + josn_str)

    producer.produce(bytes(josn_str, encoding='utf-8'))


    data = {
        "tt": "30000",
        "code": "182004",
        "mod": "18",
        "vtype": "2",
        "bitrate": "808",
        "type": "2",
        "process_time": "2020-08-04 11:30:23",
        "videoHeight": "480",
        "videoWidth": "640",
        "vid": "405",
        "src_ip": src_ip,
        "uid": "10000127",
        "uf": "3018242",
        "sd": "t-vrt-signal01.e.vhall.com:443",
        "bu": "1",
        "tag": "login",
        "app_id": "1008611",
        "errorcode": "2003",
        "ver": "1.2.4",
        "biz_role": "",
        "os": "false",
        "log_session": "13281423836",
        "_m": "",
        "p": "292966831933133600",
        "browser_name": "Chrome",
        "tf": "15366",
        "s": "13281423836",
        "biz_des01": "",
        "pf": "7",
        "biz_des02": "1",
        "nginx_utc_datetime": nginx_utc_datetime,
        "biz_id": "",
        "vfid": "405",
        "aid": "lss_9527nmsl"
    }

    josn_str = json.dumps(data)

    print("cur_date:"+nginx_utc_datetime+"; data:"+josn_str)

    producer.produce(bytes(josn_str, encoding='utf-8'))

    data = {
        "tt": "30000",
        "code": "182004",
        "mod": "18",
        "vtype": "2",
        "bitrate": "808",
        "type": "2",
        "process_time": "2020-08-04 11:30:23",
        "videoHeight": "480",
        "videoWidth": "640",
        "vid": "405",
        "src_ip": src_ip,
        "uid": "10000127",
        "uf": "3018242",
        "sd": "t-vrt-signal01.e.vhall.com:443",
        "bu": "2",
        "tag": "login",
        "app_id": "1008611",
        "errorcode": "2003",
        "ver": "1.2.4",
        "biz_role": "",
        "os": "false",
        "log_session": "13281423836",
        "_m": "",
        "p": "292966831933133600",
        "browser_name": "Chrome",
        "tf": "15366",
        "s": "13281423836",
        "biz_des01": "",
        "pf": "7",
        "biz_des02": "1",
        "nginx_utc_datetime": nginx_utc_datetime,
        "biz_id": "",
        "vfid": "405",
        "aid": "lss_9527nmsl",
        "biz_id": "9527dream"
    }

    josn_str = json.dumps(data)

    print("cur_date:" + nginx_utc_datetime + "; data:" + josn_str)

    producer.produce(bytes(josn_str, encoding='utf-8'))


    time.sleep(10)

    if(count % 1000 == 0):
        while(True):
            try:
                old_msg, exc = producer.get_delivery_report(block=False)
                if(exc is not None):
                    print("Failed to deliver msg: {}".format(repr(exc)))
                    producer.produce(bytes(old_msg.value, encoding='utf-8'))
            except Empty:
                break

producer.flush()
producer.stop()



