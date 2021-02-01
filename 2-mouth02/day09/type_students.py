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
try:
    name = input("请输入学生姓名：")
    sql = f"update school set grade=100 where name='{name}'"
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
# 关闭数据库
cur.close()
db.close()
