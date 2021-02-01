"""TCP服务端"""
from socket import *
from time import sleep
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(("0.0.0.0", 31410))
tcp_socket.listen(2)
while 1:
    print("等待客户端链接..")
    giao, addr = tcp_socket.accept()
    print("已连接客户端：", addr)
    while 1:
        data = giao.recv(5)
        if not data:
            break
        print("收到:", data.decode())
        n = giao.send(b"ok")
        sleep(0.01)
    giao.close()
