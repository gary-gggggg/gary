from threading import Lock, Thread

a = b = 1
l = Lock()


def fun():
    while 1:
        l.acquire()
        if a != b:
            print(f"a={a},b={b}")
        l.release()


t = Thread(target=fun)
t.start()
while 1:
    l.acquire()
    a += 1
    b += 1
    l.release()
t.join
