from socket import *
from multiprocessing import Process


class Server():
    data_list = []
    addr_list = []

    def __init__(self):
        self.__ic = inside_chat()
        self.giao = socket(AF_INET, SOCK_DGRAM)
        self.giao.bind(("0.0.0.0", 31514))

    def base(self):
        while 1:
            data, addr = self.giao.recvfrom(1024)
            if data in Server.data_list:
                nn = self.giao.sendto("该用户已经存在：".encode(), addr)
                break
            Server.data_list.append(data.decode())
            Server.addr_list.append(addr)
            n = self.giao.sendto("成功进入聊天室：".encode(), addr)
            self.__ic.inner_system()


class inside_chat:
    def __init__(self):
        self.gg = Server()

    def inner_system(self):
        while 1:
            intext, addr = self.gg.giao.recvfrom(1024)
            if intext==b"^&*":
                self.quit(addr)
            for i in self.gg.addr_list:
                self.gg.giao.sendto(f"{intext}".encode(), i)

    def quit(self,addr):


