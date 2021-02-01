"""用循环画图"""

number=int(input("输入整数："))
for i in range(number):
    if i==0 or i==number-1:
     print("*"* number)
    else:
     print("*%s*"%(" "*(number-2)))

