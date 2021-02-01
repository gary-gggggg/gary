"""IO多路组合演示"""
from socket import *
from select import select
file = open("my.log")
udpsocket = socket(AF_INET, SOCK_DGRAM)

tcp_socket =socket()
tcp_socket.bind(('0.0.0.0',46515))
tcp_socket.listen(5)
print("开始监控")
rs,ws,xs=select([tcp_socket],[],[],3)
print(rs)
print(ws)
print(xs)

