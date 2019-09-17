import tornado
from tornado.gen import coroutine
from tornado.web import asynchronous

from dbTest.DBAction import dba


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


class EmpHandler(tornado.web.RequestHandler):

    # @asynchronous
    @check_ai_base_arguments_exists
    # @coroutine
    async def get(self):
        try:
            employeeNumber = self.get_argument("employeeNumber")
            print("employeeNumber: " + employeeNumber)
            rs = await get_emp_data_by_id(employeeNumber)
            if rs:
                data = {
                    'employeeNumber': rs[0][0],
                    'lastName': rs[0][1],
                    'firstName': rs[0][2],
                    'email': rs[0][3]
                }

                self.write({
                    'code': 200,
                    'message': 'ok',
                    'data': data
                })

            else:
                self.write({
                    'code': 500,
                    'message': 'none data',
                    'data': {}
                })

            self.finish()

        except:
           self.write({
               "code":500,
               "msg":u"失败",
               "data":{}
           })
           self.on_finish()
           raise BaseException

# @coroutine
async def get_emp_data_by_id(param):
    sql = """SELECT 
          employeeNumber,
          lastName,
          firstName, 
          email
          FROM 
          yiibaidb.employees
          WHERE employeeNumber = %s"""
    return dba.data_inquiry_all(sql, param)