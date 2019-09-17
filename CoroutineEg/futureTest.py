#!/user/bin/env python2
# -*- coding: utf-8 -*-

from tornado import gen
from tornado.httpclient import AsyncHTTPClient
import tornado.web


class GenHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        url = 'http://www.baidu.com'
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch(url)
        s = yield gen.sleep(5) # 该阻塞还是得阻塞， 异步只是对其他链接而言的
        self.write(response.body)

class MainHandler(tornado.web.RequestHandler):
    pass

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/gen_async/", GenHandler),
    ], autoreload=True)
    application.listen(8889)
    tornado.ioloop.IOLoop.current().start()