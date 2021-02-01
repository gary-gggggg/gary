"""pysql数据的写操作
使用pymysql会自动使用事务。如果引擎不支持事务则execute后生效
若支持需commit
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
try:
    sql = "update school set grade=125 where id=1"
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
# 关闭数据库
cur.close()
db.close()
