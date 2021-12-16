# @Time : 2021/12/12 15:13
# @Author : klenq
# @File : testSqlite.py
# @Software : PyCharm


import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")
c = conn.cursor()
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''

# sql = '''
#
#     insert into company (id,name,age,address,salary)
#     values (1,'张三',32,"成都",8000)
#
# '''
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values (2,'李四',30,"重庆",15000)
#     '''

sql = '''
    select * from company
'''
c.execute(sql)

for row in c:
    print("id = ", row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3])
conn.close()
print("Create table correctly")