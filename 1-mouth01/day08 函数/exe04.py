"""创建函数,计算梯形面积.
top_base = float(input("请输入上底："))
bottom_base = float(input("请输入下底："))
height = float(input("请输入高："))
result = (top_base + bottom_base) * height / 2
print("梯形面积是：" + str(result))"""


def calculate_areas(tb, bb, h):
    """
    :param tb: top_base
    :param bb: bottom_base
    :param h: height
    :return: area of trapezoid
    """
    result = (tb + bb) * h / 2
    return result


top_base = float(input("请输入上底："))
bottom_base = float(input("请输入下底："))
height = float(input("请输入高："))
ture_one = calculate_areas(top_base, bottom_base, height)
print(ture_one)
