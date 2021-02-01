"""增加运算，输入一个4位数字，求这几个数的和
"""
# number1=number0%10
# number1_divider=number0//10
# number2=number1_divider%10
# number2_divider=number1_divider//10
# number3=number2_divider%10
# number3_divider=number2_divider//10
# number4=number3_divider%10
# print(number1+number2+number3+number4)这个不香

# number0=int(input("输入您的数字："))
# print(str(number0%10+number0//100%10+number0//10%10+number0//1000))
# 这个也不香
number0=int(input("输入您的数字："))
result=number0%10
result+=number0//10%10
result+=number0//100%10
result+=number0//1000%10
print(result)
# 这个香
