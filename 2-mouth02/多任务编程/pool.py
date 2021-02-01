from time import *
from random import random
from multiprocessing import Pool


def case(ms, sec):
    sleep(sec)  # 每次处理订单的时间
    print(ctime(), "===", ms)


# 创建进程池
pool = Pool(4)
# 将事件加入到进程池执行等待队列中
for i in range(21):
    ms = f"订单-{i}"
    pool.apply_async(case, args=(ms, random() * 10))

pool.close()
pool.join()
