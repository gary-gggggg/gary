from socket import *

ADDR = ("localhost",31403)


def main():
    while 1:
        mmsg = input("请输入问题：")
        if not mmsg:
            break
        tcp_socket = socket()
        tcp_socket.connect(ADDR)
        tcp_socket.send(mmsg.encode())
        data = tcp_socket.recv(1024)
        print("收到：", data.decode())
        tcp_socket.close()

    print("拜拜！")


if __name__ == '__main__':
    main()
