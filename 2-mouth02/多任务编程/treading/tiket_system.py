from threading import Thread
from time import sleep

ticket_list = ["t%d" % x for x in range(1, 501)]


def sell(w):
    while ticket_list:
        print(f"w{w}----{ticket_list[0]}")
        del ticket_list[0]
        sleep(0.1)


jobs = []


def windows():
    for k in range(1, 11):
        tt = Thread(target=sell, args=(k,))
        jobs.append(tt)
        tt.start()


[q.join() for q in jobs]

windows()
