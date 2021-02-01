"""创建函数,根据年月计算天数. 如果 2 月是闰年,则 29 天
平年 28
month = int(input("请输入月份:"))
if 1 <= month <= 12: if month == 2: print("29 天")
elif month == 4 or month == 6 or month == 9 or month == 11: \
print("30 天")
else:# 1 3 5 7 8 10 12
print("31 天")
else:
print("月份有误")
year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: day = 29
else: day = 28"""


def identify_fed(year):
    """
    :param year:
    :return:
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def identify_month(year, month):
    if 1>month or month > 12: return ("月份有误")
    if month == 2: return 29 if identify_fed(year) else 28
    if month == 4 or month == 6 or month == 9 or month == 11: return 30
    return 31


year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
result = identify_month(year, month)
print(result)
