"""让下列代码重复执行，输入 y 继续(不输入 y 则退出)
sex = input("请输入性别:")
if sex == "男": print("您好先生")
elif sex == "女": print("您好女士")
else: print("未知")"""
while True:
    gender=input("请输入您的性别")
    if gender=="男":
        print("您好先生")
    elif gender=="女":
        print("您好女士")
    else:
        print("未知")
    if input("请输入y继续：")!="y":
        break


