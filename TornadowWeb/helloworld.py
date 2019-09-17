#!/user/bin/env python2
# -*- coding: utf-8 -*-

# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#     ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()



import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define


#定义端口配置
from TornadowWeb.EmpHandler import EmpHandler

define('port', type=int, default=8080)

#创建视图处理器
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>hello，world</h1>")
        self.finish()

class CourseHandler(tornado.web.RequestHandler):
    def get(self,cid ):
        self.write('<h1>享学课堂-当前课程ID：%d</h1>'%(int(cid)))
        self.finish()

class CourseHandler2(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>享学课堂-Tornado教程</h1>")
        # arg = self.get_arguments('name')
        arg = self.get_query_arguments('name')
        self.write('参数是：%s' % arg)
        self.finish()


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>享学课堂-用户登录</title>
        </head>
        <body>
          <h1>享学课堂-用户登录</h1>
          <hr>

          <form action="login" method="post">
          用户名称:<input type="text" name="username"/><br>
          用户密码:<input type="password" name="password"/><br>
          <input type="submit" value="登录"/><br>
          </form>

        </body>
        </html>
        """
        self.write(html)
        self.finish()

    def post(self):
        username = self.get_argument('username', None)
        pwd = self.get_argument('password', None)
        print(username)
        print(pwd)
        self.write(u'用户名称：%s<br>密码：%s' % (username, pwd))
        self.finish()


def check_ai_base_arguments_exists(func):
    def wrapped_func(self, *args, **kwargs):
        if not {"employeeNumber"}.issubset(self.request.arguments):  # "remoteip" 无需校验
            msg = "Invalid argument: %s,please write [activity_id] " % str(self.request.arguments)
            self.finish({
                'code': 500,
                'message': u'缺少必要字段',
                'info': msg
            })
            return
        return func(self, *args, **kwargs)
    return wrapped_func


#创建路由表
urls = [(r"/", MainHandler),
        (r"/index", MainHandler),
        (r'/course/([0-9]+)', CourseHandler),
        (r"/course2", CourseHandler2),
        (r"/login", LoginHandler),
        (r"/employee", EmpHandler),]

#创建配置-开启调试模式
configs = dict(debug=True)


#自定义应用
class MyApplication(tornado.web.Application):
    def __init__(self, urls, configs):
        super(MyApplication, self).__init__(handlers=urls, **configs)


#创建服务器
def make_app():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(MyApplication(urls,configs))
    http_server.listen(9090)
    tornado.ioloop.IOLoop.current().start()

#启动服务器
if __name__ == '__main__':
    make_app()

    # print(get_emp_data_by_id(1166))