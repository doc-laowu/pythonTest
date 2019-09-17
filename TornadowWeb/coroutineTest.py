from tornado import gen
from tornado.ioloop import IOLoop

@gen.coroutine
def divide(x, y):
    return x / y

def bad_call():
    IOLoop.current().spawn_callback(divide, 1, 0)
    #IOLoop.current().run_sync(lambda: divide(1, 0))

if __name__ == "__main__":
    bad_call()