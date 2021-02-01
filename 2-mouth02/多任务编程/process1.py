import multiprocessing as mp
from time import sleep


def giao():
    print("开始第一个进程咯！！！！giao !")
    sleep(2)
    print("第一个进程结束啦！！！giao !!!")


p =mp.Process(target=giao)
p.start()
print("我猜")
sleep(3)
print("我也暗恋")
p.join()
