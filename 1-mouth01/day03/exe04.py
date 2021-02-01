"""在终端中输入课程阶段数,
显示课程名称1 显示 Python 语言核心编程2 显示 Python 高级软件技术
3 显示 Web 全栈4 显示 网络爬虫5 显示 数据分析人工
"""
course=input("输入课程阶段：")
if course=="1":
    print("Python 语言核心编程")
elif course=="2":
    print("Python 高级软件技术")
elif course=="3":
    print("Web 全栈")
elif course=="4":
    print("网络爬虫")
elif course=="5":
    print("数据分析 人工智能")
else:
    print("没有")