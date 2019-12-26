import threading

import time


class NODE:
    def __init__(self):
        self.name = "class"


class Singleton:

    _instance_lock = threading.Lock()

    def __init__(self):
        if not hasattr(self, "NODE".lower()):
            self.node = NODE()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

    @staticmethod
    def getInstance():
        obj = Singleton()
        print("node.name address: {}".format(obj.node.name))
        print("node address: {}".format(obj.node))
        print("obj address: {}".format(obj))


if(__name__ == "__main__"):

    # Singleton.getInstance()
    #
    # Singleton.getInstance()
    #
    # Singleton.getInstance()
    #
    # Singleton.getInstance()
    #
    # Singleton.getInstance()
    #
    # Singleton.getInstance()
    #
    # Singleton.getInstance()
    #
    # Singleton.getInstance()
    #
    # Singleton.getInstance()
    #
    # print("TOM AND JERRY".lower())

    # 获取当前的时间戳
    getTimstamp = lambda: int(round(time.time() * 1000))

    # 获取当前时间字符串
    currentTimeMillis = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    print("%s, %s" % (currentTimeMillis, getTimstamp()))