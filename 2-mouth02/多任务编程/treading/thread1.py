"""线程基础示例1"""
import threading as tt
from time import sleep
import os

def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放：我叼你妈")


t = tt.Thread(target=music)
t.start()
for i in range(4):
    sleep(1)
    print(os.getpid(),"我giao")
t.join()
