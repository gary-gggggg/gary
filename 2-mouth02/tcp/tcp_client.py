from socket import *

tcp_socket = socket()
ADDR = ("localhost", 56165)
tcp_socket.connect(ADDR)
while 1:
    mmsg = input(">>")
    if mmsg =="##":
        tcp_socket.close()
        break
    else:
        tcp_socket.send(mmsg.encode())
        data = tcp_socket.recv(1024)
        print("收到：", data.decode())
