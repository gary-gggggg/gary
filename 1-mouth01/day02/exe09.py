"""练习：写出下列代码表达的命题含义
        print(666 == "666")
        print(input("你爱我吗? ") == "爱")
        print(float(input("请输入你的身高：")) > 170)
    根据命题写出代码
  输入的是正数
        输入的是月份
        输入的不是偶数"""
# 命题：整数666是字符串“666” F
# 命题：你是爱我的
# 命题：你是比170高
# print(int(input("请输入一个正数："))>0)
# number01=(0<(int(input("请输入一个月份："))<12)
# print(number01 >=0<=12)
# number=int(input("请输入一个非偶数："))
# print(number%2!=0)
print(int(input("输入正数："))>0)
print(0<int(input("请输入月份："))<=12)
print(int(input("输入一个非偶数："))%2!=0)