"""
Gary
673248932@qq.com
2020.12.15

socket and process exerceise
"""
from socket import *
from multiprocessing import Process

# 服务器地址
host_address = '127.0.0.1'
port = 31415
ADDR = (host_address, port)


class Server:
    def __init__(self):
        self.gsocket = socket(AF_INET, SOCK_DGRAM)
        self.gsocket.bind(ADDR)
        self.user = {}

    def main(self):
        p = Process(target=self.logging, daemon=True)
        p.start()
        # 父进程发送管理员消息
        while 1:
            try:
                content = input("输入管理员消息：")
            except KeyboardInterrupt:
                content="exit"
            if content == "exit":
                break
            gmsg = "CHAT 管理员信息 " + content
            self.gsocket.sendto(gmsg.encode(), ADDR)

    def logging(self):
        while 1:
            data, addr = self.gsocket.recvfrom(1024)
            smsg = data.decode().split(" ", 2)
            print(smsg[0])
            if smsg[0] == "LOGIN":
                self.loginng(smsg[1].encode(), addr)
            elif smsg[0] == "CHAT":
                self.do_chat(smsg[1].encode(), smsg[2].encode())
            elif smsg[0] == "QUIT":
                self.do_quit(smsg[1].encode())

    def loginng(self, name, addr):
        if name in self.user:
            self.gsocket.sendto(b"FAIL", addr)
        else:
            self.gsocket.sendto(b"OK", addr)
            msg = f"欢迎{name.decode()}进入聊天室"
            for k, v in self.user.items():
                self.gsocket.sendto(msg.encode(), v)
            self.user[name] = addr
            print(self.user)

    def do_chat(self, name, content):
        msg = f"{name.decode()}:{content.decode()}"
        for k1, v1 in self.user.items():
            if k1 != name:
                self.gsocket.sendto(msg.encode(), v1)

    def do_quit(self, name):
        del self.user[name]
        for k1, v1 in self.user.items():
            qmsg = f"{name.decode()},已经退出聊天室"
            self.gsocket.sendto(qmsg.encode(), v1)


if __name__ == '__main__':
    m = Server()
    m.main()
