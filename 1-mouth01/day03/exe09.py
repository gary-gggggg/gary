"""练习：在终端中输入一个年份，如果是闰年为变量 day 赋值 29,否则赋值 28。
闰年条件：年份能被 4 整除但是不能被 100 整除
年份能被 400 整除
效果：
请输入年份:2020
2020 年的 2 月有 29 天"""
year=int(input("请输入一个年份："))
if year%4==0 and year%100 or year%400==0:
    #%100那里是不等于0，也就是有真值时，可以删去不等于
   print(29)
else:
    print(28)