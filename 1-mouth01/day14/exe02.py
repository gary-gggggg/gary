"""练习 2：定义函数,根据生日(年月日),计算活了多天.
输入：2010 1 1输出：从 2010 年 1 月 1 日到现在总共活了 3910"""
import time


def mac_time():
    return time.time()


def real_time(y, m, d):
    my_bd = time.strptime(f"{y}-{m}-{d}", "%Y-%m-%d")
    kk = time.mktime(my_bd)
    return kk


mmc = mac_time()
rmc = real_time(1998, 1, 17)
min=mmc-rmc
print(min/60/60/24,"天")
