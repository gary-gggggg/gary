"""pymysql数据读操作
"""
import pymysql

db_dic = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "gary",
    "charset": "utf8"
}
# 链接数据库
db = pymysql.connect(**db_dic)  # 一个链接口

# 创建游标 游标对象：执行sql得到结果的对象
cur = db.cursor()  # 打开完成

# 操作数据
sql="select name, grade from school where grade>%s;"
cur.execute(sql,[60])

#迭代获取查询结果
# for res in cur:
#     print(res)
one=cur.fetchmany(3)
print(one)

# 关闭数据库
cur.close()
db.close()