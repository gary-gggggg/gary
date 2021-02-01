from socket import *

giao = socket(AF_INET, SOCK_DGRAM)
giao.bind(("localhost", 31415))
while 1:
    deta, addr = giao.recvfrom(1024)
    print("from", addr, ":", deta.decode())
    n = giao.sendto(b"thanks", addr)
    print("发送了%dbytes" % n)


