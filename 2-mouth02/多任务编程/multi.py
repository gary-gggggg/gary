import os, sys
import multiprocessing as mp
from time import sleep


def tt():
    sleep(1)
    print("giao")
    print(os.getppid(), "==", os.getpid())


def tt1():
    sleep(2)
    print("giao1")
    print(os.getppid(), "==", os.getpid())


def tt2():
    sleep(3)
    print("giao2")
    print(os.getppid(), "==", os.getpid())

k=[]
for i in [tt, tt1, tt2]:
    p = mp.Process(target=i)
    k.append(p)
    p.start()

[i.join() for i in k]
