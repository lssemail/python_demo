#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import xlwt

sql_show_table = "show tables"
sql_desc_table = "desc "
db_ip = "localhost"
db_username = "root"
db_password = "123456"
db_name = "sboot"
db = pymysql.connect(db_ip, db_username, db_password, db_name, charset='utf8')
col_width_default = 256 * 20
cursor = db.cursor()

workbook = xlwt.Workbook(encoding="utf-8")
result = cursor.execute(sql_show_table)

print("共有:%s\t张表" % (str(result)))
for item in cursor.fetchall():
    current_index = 0
    table_name = item[0]
    book_sheet = workbook.add_sheet(table_name, cell_overwrite_ok=True)
    book_sheet.col(0).width = col_width_default
    book_sheet.col(1).width = col_width_default
    book_sheet.write(current_index, 0, "Field")
    book_sheet.write(current_index, 1, "Type")
    book_sheet.write(current_index, 2, "Null")
    book_sheet.write(current_index, 3, "Key")
    book_sheet.write(current_index, 4, "Default")
    book_sheet.write(current_index, 5, "Extra")
    data = cursor.execute("desc " + table_name)
    current_index = 1
    current_col = 0

    for row in cursor.fetchall():
        for col in row:
            book_sheet.write(current_index, current_col, col)
            current_col = current_col + 1

        current_index = current_index + 1
        current_col = 0

file_path = "".join(["C:\\Users\\Administrator\\Desktop\\", db_name, ".xls"])

workbook.save(file_path)



