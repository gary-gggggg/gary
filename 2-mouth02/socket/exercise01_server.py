"""
练习2. 基于udp循环收发程序完成

在客户端输入单词，从服务端那里得到单词解释
并打印出来，要求多个客户端可以一起查询

服务端，利用数据库dict->words表 帮助
客户端完成单词查询，将解释发送给客户端
"""
from socket import *
import pymysql


# 用于数据库的交互
class Database:
    database_args = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "dict",
        "charset": "utf8"
    }

    def __init__(self):
        self.db = pymysql.connect(**Database.database_args)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    # 查询单词解释方法
    def find_word(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        # 查到：(mean,)  没查到：None
        mean = self.cur.fetchone()
        if mean:
            return mean[0]
        else:
            return "Not Found"

class QueryWord:
    def __init__(self, host="", port=8000):
        self.host = host
        self.port = port
        self.db = Database() # 数据库处理
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.bind()

    def bind(self):
        self.address = (self.host, self.port)
        self.udp_socket.bind(self.address)

    def close(self):
        self.udp_socket.close()

    def query_word(self):
        while True:
            # 接收 发送消息 data-->bytes
            word, addr = self.udp_socket.recvfrom(1024)
            # 查询到单词解释
            mean = self.db.find_word(word.decode())
            self.udp_socket.sendto(mean.encode(), addr)

if __name__ == '__main__':
    query = QueryWord(host="0.0.0.0",port=8888)
    query.query_word()
