"""练习：在终端中输入一个整数，
如果是奇数为变量 state 赋值"奇数",否则赋值"偶数"。
效果：
请输入数字:6
state 变量存储的是：偶数"""
number=int(input("输入一个整数："))
state=number%2
if state:
    print("奇数")
else:
    print("偶数")
