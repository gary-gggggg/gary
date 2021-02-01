"""多进程tcp网络服务"""
from socket import *
from multiprocessing import Process
from dict_data import Database
from time import sleep


class HandleData:
    def __init__(self, connfd, cur):
        self.cur = cur
        self.connfd = connfd

    def recvdata(self, data):
        sdata = data.split(" ")
        print(sdata)
        if sdata[0] == "RGT":
            self.do_registerr(sdata[1], sdata[2])  # name,passwd
        elif sdata[0] == "LGI":
            self.do_loginn(sdata[1], sdata[2])
        elif sdata[0] == "CEK":
            self.do_check(sdata[1], sdata[2])
        elif sdata[0] == "HIS":
            self.do_history(sdata[1])

    def do_registerr(self, name, passwd):
        data = db.registerr(name, passwd)
        print(data)
        if data:
            self.connfd.send(b"OK")
        else:
            self.connfd.send(b"FAIL")

    def do_loginn(self, name, passwd):
        if db.loginn(name, passwd):
            self.connfd.send(b"OK")
        else:
            self.connfd.send(b"FAIL")

    def do_check(self, name, word):
        try:
            result = db.check(name, word)
            if result == "no":
                self.connfd.send(b"FAIL")
            self.connfd.send(result.encode())
            db.history(name, word)
        except:
            self.connfd.send(b"FAIL")

    def do_history(self, name):
        data = db.check_his(name)
        for r in data:
            msg = "%s %s %s" % r
            self.connfd.send(msg.encode())
            sleep(0.05)
        self.connfd.send(b"^&*")


class ServerProcess(Process):
    def __init__(self, connfd, cur):
        self.cur = cur
        self.connfd = connfd
        self.handle_data = HandleData(self.connfd, self.cur)
        super().__init__(daemon=True)

    def run(self):
        while 1:
            data = self.connfd.recv(1024).decode()
            print(data)
            if not data or data == "QUT":
                break
            self.handle_data.recvdata(data)
        self.cur.close()
        self.connfd.close()


class DictServer:
    def __init__(self, host='0.0.0.0', port=31441):
        self.port = port
        self.host = host
        self.sock = self.connecting()

    def connecting(self):
        sock = socket()
        sock.bind((self.host, self.port))
        return sock

    def server_forever(self):
        print(f"正在监听端口{self.port}")
        self.sock.listen(5)  # listen是和连接相关的所以放这里
        while 1:
            try:
                conndf, addr = self.sock.accept()
                print(f"已连接{addr}")
                cur = db.course()
            except KeyboardInterrupt:
                self.sock.close()
                return
            else:
                self.processss = ServerProcess(conndf, cur)
                self.processss.start()


if __name__ == '__main__':
    c = DictServer()
    db = Database()
    c.server_forever()
