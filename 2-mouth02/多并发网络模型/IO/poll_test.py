"""
IO多路复用演示 poll
"""
from socket import *
from select import *

# 准备一些IO
file = open("my.log")

udp_sock = socket(AF_INET,SOCK_DGRAM)

tcp_sock = socket()
tcp_sock.bind(('0.0.0.0',8888))
tcp_sock.listen(5)

# 查找字典 {fileno:IO对象}
map = {tcp_sock.fileno():tcp_sock}

p = poll()
p.register(tcp_sock,POLLIN|POLLERR)
print("开始监控")
events = p.poll() # 负责监控

# [(fileno,event)]
# 文件描述符： 系统分配给每一个IO的整数编号
print("就绪的IO：",events)


