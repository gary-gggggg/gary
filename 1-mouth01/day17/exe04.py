"""练习 2：为 sum_ data,增加打印函数执行时间的功能.
函数执行时间公式： 执行后时间 - 执行前时间"""
import time


def ectivate(fuck):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        res=fuck(*args, **kwargs)
        stop_time=time.time()
        print(stop_time-start_time)
        return res
    return wrapper



@ectivate
def sum_data(n):
    sum_value = 0
    for number in range(n): sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(10000))
