from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(("0.0.0.0", 31403))
tcp_socket.listen(2)

dicc = {"你叫什么": "我是你爸爸",
        "你是男是女": "我是一头骚猪",
        "你今年多大了": "我是你爸爸，你觉得我多大"
        }


def dic(n):
    for k, v in dicc.items():
        if n == k:
            return v
    return "这么聪明吗，竟然问出我都不知道的问题！"


def main():
    while 1:
        print("等待客户端链接..")
        giao, addr = tcp_socket.accept()
        print("已连接客户端：", addr)
        while 1:
            data = giao.recv(1024)
            if not data:
                break
            res = dic(data.decode())
            n = giao.send(res.encode())
        giao.close()


if __name__ == '__main__':
    main()
