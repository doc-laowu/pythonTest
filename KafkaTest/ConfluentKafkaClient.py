# import threading
# from confluent_kafka import Producer
#
# from config import config
# from logger import get_logger
#
# # 同步类型的静态变量
# SYNC_TYPE_CONSUMER_BUSINESS_INFO = 'consumer_activity_info_update'
# SYNC_TYPE_CONSUMER_TAG_OF_BUSINESS = 'consumer_activity_tags_update'
# SYNC_TYPE_USER_LEVEL_OF_ACTIVITY = 'statics_consumer_activity_levelandscore_update'
# SYNC_TYPE_USER_LOG_STATISTICS = 'consumer_behavior_create'
# SYNC_TYPE_USER_ACTV_STAT_INFO_VIEW = 'statics_consumer_activity_update'
#
# # 同步主题的静态变量
# SYNC_TOPIC_CONSUMER_BUSINESS_INFO = 'data_sync_consumer_business_info'
# SYNC_TOPIC_CONSUMER_TAG_OF_BUSINESS = 'data_sync_consumer_tags_of_business'
# SYNC_TOPIC_USER_LEVEL_OF_ACTIVITY = 'data_sync_user_level_of_activity'
# SYNC_TOPIC_USER_LOG_STATISTICS = 'data_sync_user_log_statistics'
# SYNC_TOPIC_USER_ACTV_STAT_INFO_VIEW = 'data_sync_user_activity_statistics_info_view'
#
# # 实力化logger
# data_sync_logger = get_logger(config.DATA_SYNC)
#
# class ConfluentKafkaClient:
#
#     # 实例化锁
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         self.SYNC_TYPE_CONSUMER_BUSINESS_INFO_PRODUCER = Producer({'bootstrap.servers': config.kafka_cluster})
#
#         self.SYNC_TYPE_CONSUMER_TAG_OF_BUSINESS_PRODUCER = Producer({'bootstrap.servers': config.kafka_cluster})
#
#         self.SYNC_TYPE_USER_LEVEL_OF_ACTIVITY_PRODUCER = Producer({'bootstrap.servers': config.kafka_cluster})
#
#         self.SYNC_TYPE_USER_LOG_STATISTICS_PRODUCER = Producer({'bootstrap.servers': config.kafka_cluster})
#
#         self.SYNC_TYPE_USER_ACTV_STAT_INFO_VIEW_PRODUCER = Producer({'bootstrap.servers': config.kafka_cluster})
#
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(ConfluentKafkaClient, "_instance"):
#             with ConfluentKafkaClient._instance_lock:
#                 if not hasattr(ConfluentKafkaClient, "_instance"):
#                     ConfluentKafkaClient._instance = object.__new__(cls)
#         return ConfluentKafkaClient._instance
#
#
#     def __del__(self):
#         # do nothing
#         pass
#
#
#     '''获取要使用的生产者和topic'''
#     @staticmethod
#     def getTopicAndProducer(self, sync_type):
#         # 要发送的topic
#         topic = None
#         # 要使用的生产者
#         producer = None
#         if (sync_type == SYNC_TYPE_CONSUMER_BUSINESS_INFO):
#             topic = SYNC_TOPIC_CONSUMER_BUSINESS_INFO
#             producer = self.SYNC_TYPE_CONSUMER_BUSINESS_INFO_PRODUCER
#
#         elif (sync_type == SYNC_TYPE_CONSUMER_TAG_OF_BUSINESS):
#             topic = SYNC_TOPIC_CONSUMER_TAG_OF_BUSINESS
#             producer = self.SYNC_TYPE_CONSUMER_TAG_OF_BUSINESS_PRODUCER
#
#         elif (sync_type == SYNC_TYPE_USER_LEVEL_OF_ACTIVITY):
#             topic = SYNC_TOPIC_USER_LEVEL_OF_ACTIVITY
#             producer = self.SYNC_TYPE_USER_LEVEL_OF_ACTIVITY_PRODUCER
#
#         elif (sync_type == SYNC_TYPE_USER_ACTV_STAT_INFO_VIEW):
#             topic = SYNC_TOPIC_USER_ACTV_STAT_INFO_VIEW
#             producer = self.SYNC_TYPE_USER_ACTV_STAT_INFO_VIEW_PRODUCER
#
#         return topic, producer
#
#
