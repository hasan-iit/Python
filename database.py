import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='',database='pydb')
# print(conn)
cur = conn.cursor()

try:
    cur.execute("update employee set name='Jahed' where id=22")
    conn.commit()
except:
    conn.rollback()


#=================================================
# try:
#     cur.execute("select * from employee")
#     result = cur.fetchall()
#     # print(result)
#     for x in result:
#         print(x)
# except:
#     conn.rollback()
#=====================================================
# sql = "insert into employee(name,id) values (%s,%s)"
# val = ('Shahed',21)
# try:
#     cur.execute(sql,val)
#     conn.commit()
# except:
#     conn.rollback()
#=====================================================


# try:
#     # cur.execute("create database pydb")
#     cur.execute("create table employee(name varchar(40),id int not null primary key)")
#     # dbs = cur.execute("show databases")
#     cur.execute("show tables")
# except:
#     conn.rollback()
# for x in cur:
#     print(x)