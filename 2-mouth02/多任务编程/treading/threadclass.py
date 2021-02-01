from threading import Thread
from time import sleep
import os


class MyThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(3):
            sleep(2)
            print(os.getpid(), "播放：我叼你妈")


m = MyThread()
m.start()
for i in range(4):
    sleep(1)
    print(os.getpid(), "我giao")
m.join()
