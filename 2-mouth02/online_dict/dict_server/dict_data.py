"""数据库的交互处理"""
import pymysql


class Database:
    db_dic = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "dict",
        "charset": "utf8"
    }

    def __init__(self):
        # 链接数据库
        self.db = pymysql.connect(**Database.db_dic)  # 一个链接口

    def course(self):
        self.cur = self.db.cursor()  # 打开完成,游标
        return self.cur

    def close(self):
        self.db.close()

    def registerr(self, name, passwd):
        sqlmsg = "insert into user_id(name,passwd) values(%s,%s);"
        try:
            self.cur.execute(sqlmsg, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def loginn(self, name, passwd):
        sqlmsg = "select name from user_id where name=%s and passwd=%s;"
        self.cur.execute(sqlmsg, [name, passwd])
        if self.cur.fetchone():
            return True
        else:
            return False

    def check(self, name, word):
        sqlmsg = "select mean from words where word=%s;"
        self.cur.execute(sqlmsg, [word])
        mean = self.cur.fetchone()[0]
        if mean:
            return mean
        else:
            return "no"

    def history(self, name, word):
        addsqlmsg = "select id from user_id where name=%s;"
        self.cur.execute(addsqlmsg, [name])
        nameid = self.cur.fetchone()[0]
        hissqlmsg = "insert into history(word,n_id) values(%s,%s);"
        try:
            self.cur.execute(hissqlmsg, [word, nameid])
            self.db.commit()
        except:
            self.db.rollback()

    def check_his(self, name):
        sql = "select u.name,his.word,his.time from user_id as u left join history as his on u.id=his.n_id where u.name=%s order by his.time desc limit 10;"
        try:
            self.cur.execute(sql,[name])
            self.db.commit()
            return self.cur.fetchall()
        except:
            self.db.rollback()
