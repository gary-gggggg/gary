from socket import *
from multiprocessing import Process
import sys

host = "0.0.0.0"
port = 45611
ADDR = (host, port)


def dealing(connfd):
    while 1:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
    connfd.close()


def main():
    ts = socket()
    ts.bind(ADDR)
    ts.listen(5)
    while 1:
        try:
            connfd, addr = ts.accept()
        except KeyboardInterrupt:
            ts.close()
            sys.exit("退出服务端")
        print("链接：", addr)
        # 创建子进程
        p = Process(target=dealing, args=(connfd,), daemon=True)
        p.start()
