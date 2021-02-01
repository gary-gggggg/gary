"""在终端中录入4个同学年龄,打印最小的年龄。"""
age=int(input("请输入您的年龄："))
age2=int(input("请输入您的年龄："))
age3=int(input("请输入您的年龄："))
age4=int(input("请输入您的年龄："))
tiny_one=age
if age2<tiny_one:
    tiny_one=age2
if age3<tiny_one:
    tiny_one=age3
if age4<tiny_one:
    tiny_one=age4
print(tiny_one)






