"""练习 3：
在终端中循环录入 5 个成绩, 最后打印平均成绩(总成绩除以人数)
效果：
请输入成绩：98
请输入成绩：83
请输入成绩：90
请输入成绩：99
请输入成绩：78
平均分：89.6"""

person=0
sum_of=0
while person<5:
    sum_of+= int(input("请输入您的成绩："))
    person+=1
print(str(sum_of/5))