"""数字累成函数"""


def giao(*args):
    sum1 = 1
    for c in args:
        sum1 *= c
    return sum1




list = [15, 46, 754, 67, 354, 6, 52,456,114,98,146,41894]
print(giao(*list))
