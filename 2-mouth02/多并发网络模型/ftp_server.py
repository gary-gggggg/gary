"""
文件服务器 服务端
"""

from socket import *
from threading import Thread
import os
from time import sleep

# 文件库
FTP = "/home/tarena/FTP/"


# 具体处理客户端事务
class Handle:
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        files = os.listdir(FTP)
        if files:
            self.connfd.send(b"OK")
            sleep(0.1)

            # 组合所有文件名
            data = "\n".join(files)
            self.connfd.send(data.encode())
        else:
            self.connfd.send(b"FAIL")

    # 将请求分情况讨论
    def request(self, data):
        if data == "LIST":
            self.do_list()
        elif data[:3] == "GET":
            filename = data.split(" ")[-1]
            self.do_get(filename)
        elif data[:3] == "PUT":
            filename = data.split(" ")[-1]
            self.do_download(filename)
        elif data == "EXIT":
            pass

    def do_get(self, filename):
        try:
            file = open(FTP + filename, 'rb')
        except:
            self.connfd.send(b"Fail")
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            while 1:
                data = file.read(1024)
                if not data:
                    break
                self.connfd.send(data)
            sleep(0.1)
            self.connfd.send(b"^&*")

    def do_download(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send(b"giao")
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            file = open(FTP + filename, "wb")
            while 1:
                data_f = self.connfd.recv(1024)
                if data_f == b"##^&*":
                    break
                file.write(data_f)
            file.close()


# 为每个客户端创建线程
class ClientThread(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        self.handle = Handle(connfd)
        super().__init__(daemon=True)

    def run(self):
        while True:
            # data客户端发送过来的请求
            data = self.connfd.recv(1024).decode()
            if not data:
                break
            self.handle.request(data)
        self.connfd.close()


# 并发服务类
class ConcurrentServer:
    """
    提供并发服务
    """

    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.__sock = self.__create_socket()

    # 创建套接字
    def __create_socket(self):
        tcp_socket = socket()
        tcp_socket.bind(self.address)
        return tcp_socket

    # 启动服务
    def serve_forever(self):
        print("Listen the port %d" % self.port)
        self.__sock.listen(5)
        while True:
            connfd, addr = self.__sock.accept()
            print("Connect from", addr)
            # 为客户端创建线程
            thread = ClientThread(connfd)
            thread.start()


if __name__ == '__main__':
    server = ConcurrentServer(host="0.0.0.0", port=8882)
    server.serve_forever()  # 启动服务
