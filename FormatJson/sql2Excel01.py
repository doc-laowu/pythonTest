# --*-- coding:utf8 --*--
import pymysql, xlwt
from datetime import datetime


def export_excel(table_name):
    # 连接数据库，查询数据
    host, user, passwd, db = '*', '*', '*', '*'
    conn = pymysql.connect(user=user, host=host, port=3306, passwd=passwd, db=db, charset='utf8')
    cur = conn.cursor()


    sql = """SELECT * FROM users"""


    cur.execute(sql)  # 返回受影响的行数

    fields = [field[0] for field in cur.description]  # 获取所有字段名
    all_data = cur.fetchall()  # 所有数据

    # 写入excel
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')

    for col, field in enumerate(fields):
        sheet.write(0, col, field)

    row = 1
    for data in all_data:
        for col, field in enumerate(data):
            field_temp = field
            if (isinstance(field, datetime)):
                field_temp = datetime.strftime(field, '%Y-%m-%d %H:%M:%S')
            sheet.write(row, col, field_temp)
        row += 1
    book.save("%s.xls" % table_name)

if __name__ == '__main__':
    export_excel('app1_book')
