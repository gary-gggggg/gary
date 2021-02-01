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
list1 = [
        ("张三", 21, 'male', 65),
        ("李四", 18, 'female', 47),
        ("王五", 16, 'others', 94)
    ]
try:
    sql = "insert into school (name,age,gender,grade) values (%s,%s,%s,%s);"
    cur.executemany(sql, list1)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
# 关闭数据库
cur.close()
db.close()
