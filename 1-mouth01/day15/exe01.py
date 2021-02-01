"""
练习：创建函数，在终端中录入 int 类型成绩。如果格式不正确，重新输入。
效果： score = get_score()
print("成绩是：%d"%score)
"""


def get_score():
    while 1:
        try:
            score = int(input("请输入您的成绩"))
            return score
        except:
            print("输入有误")


score = get_score()
print("成绩是：%d" % score)
