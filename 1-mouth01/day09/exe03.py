""""""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


func01(*"随悟空")

list01 = [1, 5, 3, 789, 15]


def func02(*args):
    print(args)


func02()
func02(1)
func02(1, 8, 1)
func02(*list01)
