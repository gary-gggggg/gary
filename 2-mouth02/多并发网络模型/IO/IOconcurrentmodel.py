"""IO并发模型 基于select方法 tcp"""
from socket import *
from select import select

tcpsocket = socket()
tcpsocket.bind(('0.0.0.0', 56165))
tcpsocket.listen(5)
rlist = [tcpsocket]
wlist = []
xlist = []
tcpsocket.setblocking(False)
# 循环监控发生的IO事件
while 1:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r == tcpsocket:
            confonde, addr = r.accept()
            print("connecting:", addr)
            confonde.setblocking(False)
            rlist.append(confonde)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
