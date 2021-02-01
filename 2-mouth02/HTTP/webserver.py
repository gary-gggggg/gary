"""API"""
from socket import socket
from time import sleep
from select import *
import re


class Dealing:
    def __init__(self, connfd, html):
        self.html = html
        self.connfd = connfd
        self.filedict = {"/": "amusement.html",
                         "/amusement": "amusement.html",
                         "/learn": "learn.html",
                         "/setpuwebsite": "setpuwebsite.html",
                         "/shop": "shop.html",
                         "/use": "use.html"}


    def recev_date(self, n):
        for k, v in self.filedict.items():
            if n == k:
                try:
                    file= open(self.html + v, "rb")
                except FileNotFoundError:
                    response = "HTTP/1.1 404 OK\r\n"
                    response += "Content-Type:text/html\r\n"
                    response += "\r\n"
                    response += "sorry....."
                    response.encode()
                else:
                    response = "HTTP/1.1 200 OK\r\n"
                    response += "Content-Type:text/html\r\n"
                    response += "\r\n"
                    response = response.encode() + file.read()
                finally:
                    self.connfd.send(response)

    def handle(self):
        data = self.connfd.recv(1024 * 10).decode()
        pattern = r"[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, data)
        if result:
            info = result.group("info")
            print("请求内容：", info)
            self.recev_date(info)



class WebServer:
    def __init__(self, host='0.0.0.0', html='/home/tarena/mouth02/HTTP/static/',
                 port=31410):
        self.port = port
        self.html = html
        self.host = host
        self.sock = self.create_socket()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    def start(self):
        self.sock.listen(5)
        print("listen to port:", self.port)
        self.rlist.append(self.sock)
        # I/O多路复用模型
        while 1:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    self.connect()
                else:
                    self.__dealiing = Dealing(r,self.html)
                    self.__dealiing.handle()


    def create_socket(self):
        sock = socket()
        self.address = (self.host, self.port)
        sock.bind(self.address)
        sock.setblocking(False)  # 设置套接字非阻塞
        return sock

    def connect(self):
        connfd, addr = self.sock.accept()
        print("connecting with", addr)
        connfd.setblocking(False)
        self.rlist.append(connfd)


if __name__ == '__main__':
    httpd = WebServer()
    httpd.start()
