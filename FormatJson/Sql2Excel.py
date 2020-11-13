# --*-- coding:utf8 --*--
import pymysql, openpyxl
from datetime import datetime


def export_excel(table_name):
    # 连接数据库，查询数据
    host, user, passwd, db = '*', '*', '*', '*'
    conn = pymysql.connect(user=user, host=host, port=3306, passwd=passwd, db=db, charset='utf8')
    cur = conn.cursor()


    sql = """SELECT * FROM users"""


    cur.execute(sql)

    fields = [field[0] for field in cur.description]  # 获取所有字段名
    all_data = cur.fetchall()  # 所有数据

    # 写入excel
    index = 0
    sheetName = "%d" % index
    book = openpyxl.Workbook()
    book.create_sheet(title=sheetName, index=index)
    sheets = book.sheetnames
    sheet = book[sheets[index]]

    # for col, field in enumerate(fields):
    #     sheet.cell(1, col+1, field)

    row = 2
    row_index = 2
    for data in all_data:

        # 当满10万行的时候切换一个sheet
        if((row-1)%100000 == 0):
            row_index = 1
            index += 1
            sheetName = "%d" % index
            book.create_sheet(title=sheetName, index=index)
            sheets = book.sheetnames
            sheet = book[sheets[index]]
            print("row_index:%d" % row)

        for col, field in enumerate(data):
            field_temp = field
            if (isinstance(field, datetime)):
                field_temp = datetime.strftime(field, '%Y-%m-%d %H:%M:%S')
            sheet.cell(row_index, col+1, field_temp)
        row += 1
        row_index += 1

    print(row)
    book.save("%s.xlsx" % table_name)
    book.close()

if __name__ == '__main__':
    export_excel('[房间5695]导出记录')
