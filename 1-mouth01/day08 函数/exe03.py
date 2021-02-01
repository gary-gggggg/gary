"""创建函数,根据课程阶段计算课程名称. number = input("请输入课程阶段数：")
if number == "1": print("Python 语言核心编程")
elif number == "2": print("Python 高级软件技术")
elif number == "3": print("Web 全栈")
elif number == "4": print("网络爬虫")
elif number == "5": print("数据分析、人工智能")"""


def identify(nubmer):
    dic_course = {"1": "Python 语言核心编程", "2": "Python 高级软件技术","3": "Web 全栈", "4": "网络爬虫","5": "数据分析、人工智能"}
    if nubmer in dic_course:
        return dic_course[nubmer]


number = input("请输入课程阶段数：")
real_one = identify(number)
print(real_one)
