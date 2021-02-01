from socket import *

ADDR = ("localhost", 31411)


def send_pic(tcp_socket, fff):
    file = open(fff, "rb")
    while 1:
        wenjian = ff.read(1024)
        if not wenjian:
            break
        tcp_socket.send(wenjian)
        data = tcp_socket.recv(1024)
        print("收到：", data.decode())
    file.close()


def main(ff):
    fileneme = f"/home/tarena/mouth02/client/{ff}"
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    send_pic(tcp_socket, fileneme)
    tcp_socket.close()


if __name__ == '__main__':
    main("wife.jpg")
