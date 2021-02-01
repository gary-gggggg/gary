from threading import Thread, Lock

l = Lock()
lo = Lock()


def odd():
    for i in range(1, 53, 2):
        l.acquire()
        print(i, end="")
        print(i + 1, end="")
        lo.release()


def zimu():
    for i in range(65, 91):
        r = chr(i)
        lo.acquire()
        print(r, end="")
        l.release()


tt = Thread(target=odd)
ttt = Thread(target=zimu)
lo.acquire()
tt.start()
ttt.start()
tt.join()
ttt.join()
