"""练习 1
：需求：
定义函数，在列表中查找奇数
定义函数，在列表中查找能被 3 或 5 整除的数字
步骤：1. 根据需求，写出函数。
2. 因为主体逻辑相同,核心算法不同.
所以使用函数式编程思想(分、隔、做)创建通用函数 find_all
3. 在当前模块中调用"""

list1 = [1, 2, 64, 9, 31, 96745, 4, 451, 67, 7]


def odd(nn):
    return nn % 2 != 0


def tof(nnn):
    return nnn % 3 == 0 or nnn % 5 == 0


def find(l):
    for i in list1:
        if l(i):
            yield i


a = find(odd)
for t in a:
    print(t)
