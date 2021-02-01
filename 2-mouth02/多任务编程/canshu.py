import multiprocessing as mp
from time import sleep


def ggg(s, nn):
    for i in range(3):
        sleep(s)
        print(f"I AM{nn}")
        print("I'm handsome")


tt = mp.Process(target=ggg, args=(3, "gary"),)
tt.start()
tt.join()
