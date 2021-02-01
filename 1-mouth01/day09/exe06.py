"""实际参数
形式参数"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


dict01 = {"p3": 20, "p1": 50, "p2": 35}
func01(**dict01)


def func02(**kwargs):
    print(kwargs)

func02(p1=88,p3=456,pp=1256)