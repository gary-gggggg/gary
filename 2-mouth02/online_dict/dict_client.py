"""客户端请求操作（1和2界面）"""
from socket import *
import sys
from time import sleep


class Handel:
    def __init__(self, host='localhost', port=31441):
        self.port = port
        self.host = host
        self.sock = self.connecting()

    def connecting(self):
        sock = socket()
        sock.connect((self.host, self.port))
        return sock

    def login(self):
        name = input("请输入您的用户名账号(账号中不能存在空格)：")
        passwd = input("请输入您的密码：")
        msg = f"LGI {name} {passwd}".encode()
        self.sock.send(msg)
        result = self.sock.recv(1024).decode()
        if result == "OK":
            print("登录成功!!")
            return name
        else:
            print("请输入正确的账号和密码！")

    def registerr(self, name, passwd):
        msg = f"RGT {name} {passwd}".encode()
        self.sock.send(msg)
        result = self.sock.recv(1024).decode()
        print(result)
        if result == "OK":
            print("注册成功！！！,欢迎成为羽锐国际的一员")
            return name
        else:
            print("账号有点问题呦！！！")

    def quit(self):
        self.sock.send(b"QUT")

    def check(self,name):
        while 1:
            word=input("请输入您想要搜索的单词(按^&*退出）：")
            if word=="^&*":
                break
            msg=f"CEK {name} {word}".encode()
            self.sock.send(msg)
            result=self.sock.recv(1024*10).decode()
            if result=="FAIL":
                print("没有这个单词呦！")
                continue
            print(f"{word}:{result}")



    def hitory(self,name):
        msg=f"HIS {name}"
        self.sock.send(msg.encode())
        while 1:
            data=self.sock.recv(1024).decode()
            if data=="^&*":
                break
            print(data)



class ClientView:
    def __init__(self):
        self.handel = Handel()

    def select_meun1(self):
        while 1:
            print("欢迎来到超级无敌词典!!!")
            print("")
            print("登录 请按1键")
            print("注册 请按2键")
            print("退出 请按3键")
            print("")
            try:
                number = int(input("请按照提示输出您需要的服务:"))
            except:
                print("请输入正确的选项！")
            else:
                if number == 1:
                    name = self.handel.login()
                    if name:
                        self.select_meun2(name)
                elif number == 2:
                    name = input("请输入您想要的用户名账号(账号中不能存在空格)：")
                    passwd = input("请输入您的密码：")
                    if " " in name or " " in passwd:
                        continue
                    self.handel.registerr(name, passwd)
                elif number == 3:
                    self.handel.quit()
                    sys.exit("您已成功退出程序")
                else:
                    print("请输入正确的选项！")


    def main(self):
        while 1:
            self.select_meun1()

    def select_meun2(self,name):
        while 1:
            print("")
            print("查询单词 请按1键")
            print("历史记录 请按2键")
            print("注销 请按3键")
            print(f"欢迎{name}")
            number = int(input("请按照提示输出您需要的服务:"))
            if number == 1:
                self.handel.check(name)
            elif number == 2:
                self.handel.hitory(name)
            elif number == 3:
                break


if __name__ == '__main__':
    c = ClientView()
    c.main()
