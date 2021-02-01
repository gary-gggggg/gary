from socket import *
ADDR = ("localhost", 31410)

while 1:
    mmsg = input(">>")
    if not mmsg:
        break
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(mmsg.encode())
    data = tcp_socket.recv(1024)
    print("收到：", data.decode())
    tcp_socket.close()

print("拜拜！")