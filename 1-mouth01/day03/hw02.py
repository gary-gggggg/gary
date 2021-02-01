"""根据年龄，输出对应的人生阶段。
            年龄       ⼈⽣阶段
            0-6 岁      童年
            7-17 岁     少年
            18-40 岁    ⻘年
            41-65 岁    中年
            65 岁之后    ⽼年
        步骤:
            终端中获取年龄
            显示人生阶段"""
age=int(input("请输入您的年龄："))
if age>=65:
    print("老年")
elif 41<=age:
    print("中年")
elif 18 <= age:
    print("青年")
elif 7 <= age:
    print("少年")
else:
    print("童年")