from threading import Thread
from socket import *
import sys


class Client:
    ADDR = ("localhost", 31514)

    def __init__(self):
        self.ss = socket()
        self.ss.connect(Client.ADDR)
    def main(self):
        while 1:
            msg=input("请输入您想要输入的话：")
            if msg=="^&*":
                self.ss.close()
                break
            self.ss.send(msg.encode())

if __name__ == '__main__':
    cc=Client()
    cc.main()