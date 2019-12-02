import threading


class node:
    def __init__(self):
        self.name = "class"


class Singleton:

    _instance_lock = threading.Lock()

    def __init__(self):
        if not hasattr(self, "node"):
            self.node = node()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

    @staticmethod
    def getInstance():
        obj = Singleton()
        print("node address: {}".format(obj.node))
        print("obj address: {}".format(obj))


if(__name__ == "__main__"):

    Singleton.getInstance()

    Singleton.getInstance()

    Singleton.getInstance()

    Singleton.getInstance()

    Singleton.getInstance()

    Singleton.getInstance()

    Singleton.getInstance()

    Singleton.getInstance()

    Singleton.getInstance()