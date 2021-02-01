import pymysql
from socket import *

db_dic = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "dict",
    "charset": "utf8"
}

db = pymysql.connect(**db_dic)
cur = db.cursor()
giao = socket(AF_INET, SOCK_DGRAM)
giao.bind(("0.0.0.0", 31414))
while 1:
    while 1:
        deta, addr = giao.recvfrom(1024)
        try:
            sql = "select mean from words where word=%s"
            cur.execute(sql, [deta.decode()])
            qq = cur.fetchone()[0]
            n = giao.sendto(qq.encode(), addr)
        except Exception as e:
            k = giao.sendto("没有该单词".encode(), addr)
    cur.close()
    db.close()
