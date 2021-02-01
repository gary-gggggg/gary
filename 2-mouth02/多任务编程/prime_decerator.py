import time
import multiprocessing as mp


def times(func):
    def giao(*args, **kwargs):
        star_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("时间:", end_time - star_time)
        return res

    return giao()


# 自定义进程
# 求100000以内质数之和
class Prime(mp.Process):
    @staticmethod
    def calculate(n):  # 判断一个数是否为质数
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    def __init__(self, begin, end):
        """

        :param begin: 开始数字
        :param end: 结束数字
        """
        self.end = end
        self.begin = begin
        super().__init__()

    # 从begin到end之间的质数之和
    def run(self):
        prime = []
        for i in range(self.begin, self.end):
            if Prime.calculate(i):
                prime.append(i)
            print(sum(prime))


@times
def process_4():
    jobs = []
    for i in range(1, 100001, 500):
        qq = Prime(i, i + 500)
        jobs.append(qq)
        qq.start()
    [i.join() for i in jobs]

process_4()

