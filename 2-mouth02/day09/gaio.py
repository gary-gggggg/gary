import pymysql

db_dic = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}
# 链接数据库
db = pymysql.connect(**db_dic)  # 一个链接口

# 创建游标 游标对象：执行sql得到结果的对象
cur = db.cursor()  # 打开完成

# 操作数据
try:
    sql="select pic from pic where id=4"
    cur.execute(sql)
    p=cur.fetchone()[0]
    with open("jiqi.jpg","wb") as qq:
        qq.write(p)
except Exception as e:
    print(e)



# 关闭数据库
cur.close()
db.close()