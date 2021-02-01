from socket import *
a=input("请输入IP地址：")
b=input("请输入端口：")
ADDR = ("176.17.12.178", 31414)
giao = socket(AF_INET, SOCK_DGRAM)

while 1:
    m = input(":")
    if not m:
        break
    else:
        giao.sendto(m.encode(), ADDR)
        d, a = giao.recvfrom(1024)
        print("意思是", d.decode())

giao.close()
