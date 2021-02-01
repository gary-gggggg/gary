"""定义函数,根据总两数,计算几斤零几两.: 提示：使用容器包装需要返回的多个数据
total_liang = int(input("请输入两:"))
jin = total_liang // 16
liang = total_liang % 16
print(str(jin) + "斤零" + str(liang) + "两")"""


def calculate_jin_liang(tt):
    """
    :param jin:
    :param liang:
    :return:
    """
    jin = total_liang // 16
    liang = total_liang % 16
    return jin, liang


total_liang= int(input("请输入两:"))
jin,liang= calculate_jin_liang(total_liang)
print(str(jin), "jin", str(liang), "liang")
