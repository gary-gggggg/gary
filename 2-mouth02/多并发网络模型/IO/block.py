from socket import *
from time import sleep,ctime

socketfd = socket()
socketfd.bind(('0.0.0.0', 56123))
socketfd.listen(5)
file=open("my.log","a")
# 设置套接字非阻塞
socketfd.settimeout(3)

while 1:
    print("waiting for client")
    try:
        confoned, addr = socketfd.accept()
        print("connecting:", addr)
    except BlockingIOError as e:
        sleep(2)
        msg=f"{ctime()}{e}\n"
        file.write(msg)
    except TimeoutError as e:
        msg = f"{ctime()}{e}\n"
        file.write(msg)
    else:
        data = confoned.recv(1024)
        print(data.decode())
