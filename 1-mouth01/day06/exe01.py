year = int(input("输入年份："))
month=int(input("输入月份："))
day=int(input("输入几号："))

fgiao=29 if year % 4 == 0 and year % 100 != 0 else 28
days_of_month=(31,fgiao,31,30,31,30,31,31,30,31,30,31)
days=sum(days_of_month[:month-1])+day
print(days)