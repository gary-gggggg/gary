from threading import Thread
from time import sleep


def fun(sec, name):
    print("lalalal")
    sleep(sec)
    print(f"{name}线程执行啦")


jobs = []
for i in range(5):
    t = Thread(target=fun,
               args=(1,),
               kwargs={"name": f"T-{i}"})
    jobs.append(t)
    t.start()
[q.join() for q in jobs]
