"""定义函数,根据小时、分钟、秒,计算总秒数
调用：提供小时、分钟、秒
调用：提供分钟、秒
调用：提供小时、秒
调用：提供分钟
"""


def calculate_cent(n1=0, n2=0, n3=0):
    """
    一给我里giaogiao !
    :param n1: 小时
    :param n2: 分钟
    :param n3: 秒
    :return: 总秒数
    """
    return n1 * 3600 + n2 * 60 + n3



print(calculate_cent(n2=3))

