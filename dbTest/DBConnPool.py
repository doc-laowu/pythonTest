import threading
import pymysql
from DBUtils.PooledDB import PooledDB


class DBConnPool():

    # 实例化锁
    _instance_lock = threading.Lock()

    def __init__(self):
        self.pool = PooledDB(creator=pymysql, mincached=1, maxcached=10, maxconnections=100,
                             blocking=True,host= "127.0.0.1", port=3306, user='root',
                             passwd='123456',db='yiibaidb', charset='utf8',)


    def __new__(cls, *args, **kwargs):
        if not hasattr(DBConnPool, "_instance"):
            with DBConnPool._instance_lock:
                if not hasattr(DBConnPool, "_instance"):
                    DBConnPool._instance = object.__new__(cls)
        return DBConnPool._instance

    def __del__(self):
        #销毁连接池
        self.pool.close()

    # 获取连接
    def get_connection(self):
        return self.pool.connection();