from threading import Thread
from socket import *
import sys


class Dealing:
    def __init__(self):
        ADDR = ("localhost", 31514)
        self.ss = socket()
        self.ss.connect(ADDR)

    def recvinstruction(self, number):
        if int(number) == 1:
            msg = "UPLOAD"
        elif int(number) == 2:
            msg = "DOWNLOAD"
        elif int(number) == 3:
            msg = "CHECK"
        elif int(number) == 4:
            msg = "QUIT"
        self.ss.send(msg.encode())


class Client:
    def __init__(self):
        self.dealing = Dealing()

    def main(self):
        while 1:
            self.show_menu()
            self.select_menu()

    def show_menu(self):
        print("输入 1 :上传文件。")
        print("输入 2 :下载文件。")
        print("输入 3 :查看云文件库文件。")
        print("输入 4 :退出服务。")
        print("")
        self.select_menu()

    def select_menu(self):
        number = input("请按数字选择您需要的服务：")
        self.dealing.recvinstruction(number)


if __name__ == '__main__':
    cc = Client()
    cc.main()
