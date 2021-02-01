"""聊天室客户端"""
from socket import *
from multiprocessing import Process
import sys


class Client:
    def __init__(self):
        self.SREVER_ADDR = ("localhost", 31415)
        self.gsocket = socket(AF_INET, SOCK_DGRAM)

    def main(self):
        while 1:
            name = input("请输入姓名:")
            msg = "LOGIN " + name
            n = self.gsocket.sendto(msg.encode(), self.SREVER_ADDR)
            res, addr = self.gsocket.recvfrom(1024)
            if res == b"OK":
                print("您已经进入聊天室！")
                self.send_chat(name)
            else:
                print("该名称已经存在！")

    def send_chat(self, name):
        p = Process(target=self.recv_chat, daemon=True)
        p.start()
        while 1:
            try:
                content = input("请输入您要说的话：")
            except KeyboardInterrupt:
                content = "^&*"
            if content == "^&*":
                cmsg = "QUIT " + name
                self.gsocket.sendto(cmsg.encode(), self.SREVER_ADDR)
                sys.exit("您已退出聊天室")
            else:
                cmsg = f"CHAT {name} {content}"
                self.gsocket.sendto(cmsg.encode(), self.SREVER_ADDR)

    def recv_chat(self):
        while 1:
            data, addr = self.gsocket.recvfrom(1024)
            msg = "\n" + data.decode() + "\n请输入您要说的话："
            print(msg, end="")


if __name__ == '__main__':
    cc = Client()
    cc.main()
