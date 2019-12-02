import time
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': '192.168.52.129:9092,192.168.52.130:9092,192.168.52.131:9092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic, msg.partition()))

for data in range(20000):
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    msg = """{"consumer_uid": "83200002", "activity_id": "271565014", "business_uid": "5300002", "bu": 0, 
    "watch_live_time": 491, "watch_replay_time": 0, "watch_replay_count": "", "chat_count": 0, "share_count": 1, 
    "invite_friends_count": 0, "attention_goods_count": "", "market_channel": "0", "is_concern": "0", "is_apply": "1", 
    "is_order": "1", "computer_common_browser": "", "times_computer_common_browser": "", "mobile_common_browser": "", 
    "times_mobile_common_browser": "", "first_visited_at": "2019-11-22 18:59:25", "last_visited_at": "2019-11-22 19:21:15", 
    "src_ip": "1.119.193.36", "country": "\u4e2d\u56fd", "province": "\u5317\u4eac", "city": "\u5317\u4eac", "device": "Windows", 
    "guide_page_leave_at": "2019-11-22 19:21:15", "guide_page_join_at": "2019-11-22 18:59:25", 
    "browser": "Chrome", "dc_updated_time": "2019-11-25 09:55:41", "score": 6.0, "t_version": "v_0"}"""
    p.produce('data_sync_user_log_statistics', msg.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()





