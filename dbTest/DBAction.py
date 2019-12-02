import traceback

import pymysql

from dbTest.DBConnPool import DBConnPool


class DBAction():
    #连接池对象
    def __init__(self):
        #建立和数据库系统的连接
        global db_pool_ins
        db_pool_ins = None
        if db_pool_ins == None:
            db_pool_ins = DBConnPool()
            print(db_pool_ins)
        self.conn = db_pool_ins.get_connection()
        #获取操作游标
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close_database(self):
        self.cursor.close()
        self.conn.close()

    def data_operate(self, sql, params=()):
        '''
        数据的插入，更新，删除
        :param database:
        :param sql:
        :return: 成功：0，失败：1
        '''
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
            return 0
        except:
            print("sql is %s, params is %s error. %s" % (sql, params, traceback.format_exc()))
            self.conn.rollback()
            raise Exception

    def data_operate_many(self, sql, params=()):
        '''
        数据的插入，更新，删除
        :param sql:
        :param params:
        :return: 成功：0，失败：1
        '''
        #执行sql语句
        self.cursor.executemany(sql, params)
        #提交到数据库执行
        self.conn.commit()

    def data_operate_count(self, sql, params=()):
        '''
        数据的插入，更新，删除
        :return: 受影响的条数
        '''
        #执行sql语句
        count = self.cursor.execute(sql, params)
        #提交到数据库执行
        self.conn.commit()
        return count

    def data_inquiry(self, sql, size=10, params=()):
        '''
        :param database:
        :param sql:
        :return: ((),(),...,())
        '''
        self.cursor.execute(sql, params)
        result = self.cursor.fetchmany(size)
        return result

    def data_inquiry_all(self, sql, params=()):
        '''
        :param database:
        :param sql:
        :return: ((),(),...,())
        '''
        self.cursor.execute(sql, params)
        result = self.cursor.fetchall()

        return result

    def commit(self):
        self.conn.commit()

global dba
dba = DBAction()

exp3 = lambda x:x+1 if not 2==1 else 0