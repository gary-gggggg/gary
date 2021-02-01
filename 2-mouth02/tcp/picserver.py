from socket import *
from time import localtime


def recv_pic(giao):
    r_n = "%s-%s-%s" % localtime()[:3] + "jpg"
    filename = f"/home/tarena/mouth02/server/{r_n}"
    file = open(filename, "wb")
    while 1:
        data = giao.recv(1024)
        if not data:
            n = giao.send(b"ok")
            break
        file.write(data)
    file.close()


def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0", 31411))
    tcp_socket.listen(2)
    while 1:
        print("等待客户端链接..")
        giao, addr = tcp_socket.accept()
        print("已连接客户端：", addr)
        recv_pic(giao)


if __name__ == '__main__':
    main()
