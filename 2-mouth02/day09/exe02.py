import pymysql
import re

filename = "/home/tarena/mouth02/day03/dict.txt"
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


# 得到数据
def giao():
    date = []
    ff = open(filename)
    for i in ff:
        word_list = re.findall(r"(\w+)\s+(.*)", i)
        date.append(word_list[0])
    ff.close()
    return date


# 操作数据
def main():
    try:
        gg = giao()
        sql = "insert into words(word,mean) values(%s,%s)"
        cur.executemany(sql, gg)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

# 关闭数据库
    cur.close()
    db.close()

if __name__ == '__main__':
    main()
