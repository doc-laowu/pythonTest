#-*- coding: UTF-8 -*-
from queue import Empty

import time
from pykafka import KafkaClient

client = KafkaClient(hosts="192.168.52.129:9092,192.168.52.130:9092,192.168.52.131:9092")
topic = client.topics['data_sync_user_log_statistics']

producer = topic.get_producer(delivery_reports=True)

count = 0
for i in range(10000):
    count += 1
    producer.produce(bytes("""{"consumer_uid": "83200002", "activity_id": "271565014", "business_uid": "5300002", "bu": 0, "watch_live_time": 491, 
    "watch_replay_time": 0, "watch_replay_count": "", "chat_count": 0, "share_count": 1, "invite_friends_count": 0, "attention_goods_count": "", 
    "market_channel": "0", "is_concern": "0", "is_apply": "1", "is_order": "1", "computer_common_browser": "", "times_computer_common_browser": "", 
    "mobile_common_browser": "", "times_mobile_common_browser": "", "first_visited_at": "2019-11-22 18:59:25", 
    "last_visited_at": "2019-11-22 19:21:15", "src_ip": "1.119.193.36", "country": "\u4e2d\u56fd", "province": "\u5317\u4eac", 
    "city": "\u5317\u4eac", "device": "Windows", "guide_page_leave_at": "2019-11-22 19:21:15", "guide_page_join_at": "2019-11-22 18:59:25", 
    "browser": "Chrome", "dc_updated_time": "2019-11-25 09:55:41", "score": 6.0, "t_version": "v_0"}""", encoding='utf-8'))
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



