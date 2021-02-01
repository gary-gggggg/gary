import os
import multiprocessing as mp

data = os.path.getsize("dict.txt")


def up_def():
    up = open("up_dict.txt", "wb")
    ff = open("dict.txt", "rb")
    n = data // 2
    while n >= 1024:
        up.write(ff.read(1024))
        n -= 1024
    else:
        up.write(ff.read(n))
    ff.close()
    up.close()


def down_def():
    ff = open("dict.txt", "rb")
    dp = open("bot.txt", "wb")
    ff.seek(data // 2)
    while 1:
        dd = ff.read(1024)
        if not dd:
            break
        dp.write(dd)
    dp.close()
    ff.close()


p = mp.Process(target=up_def)
p.start()

down_def()

p.join()
