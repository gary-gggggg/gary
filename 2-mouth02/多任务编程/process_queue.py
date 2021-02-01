"""进程间通信示例"""
from multiprocessing import Process
from multiprocessing import Queue

q = Queue()


def handle():
    aa = q.get()
    try:
        eval(aa)
    except Exception as e:
        print("语法有误！")
        print(e)


p2 = Process(target=handle, daemon=True)
p2.start()
while 1:
    aa = input("请输入语句：")
    if aa=="exit":
        break
    q.put(aa)
p2.join()
