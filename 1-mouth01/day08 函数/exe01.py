"""：创建计算治愈比例的函数
confirmed = int(input("请输入确诊人数:"))
cure = int(input("请输入治愈人数:"))
cure_rate = cure / confirmed * 100
print("治愈比例为" + str(cure_rate) + "%"""


def divide(number1, number2):
    """
    :param number1: confirmed number
    :param number2: cured number
    :return: cure ratio
    """
    result = number2 / number1 * 100
    return result


number1 = int(input("enter the confirmed number："))
number2 = int(input("enter the cured number："))
print(str(divide(number1,number2))+"%")

