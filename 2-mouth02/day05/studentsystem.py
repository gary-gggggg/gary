"""
env: python3.6  pycharm
"""
import re  # 导入正则表达式模块
import os  # 导入操作系统模块

filename = "students.txt"  # 定义保存学生信息的文件名


def menu():
    # 输出菜单
    print('''
    ╔———————学生信息管理系统————————╗
    │                                              │
    │   =============== 功能菜单 ===============   │
    │                                              │
    │   1 录入学生信息                             │
    │   2 查找学生信息                             │
    │   3 删除学生信息                             │
    │   4 修改学生信息                             │
    │   5 排序                                     │
    │   6 统计学生总人数                           │
    │   7 显示所有学生信息                         │
    │   0 退出系统                                 │
    │  ==========================================  │
    │  说明：通过数字键选择菜单          │
    ╚———————————————————————╝
    ''')


def main():
    ctrl = True  # 标记是否退出系统
    while ctrl:
        menu()  # 显示菜单
        option = input("请选择：")  # 选择菜单项
        option_str = re.sub("\D", "", option)  # 提取数字
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            if option_str == '0':  # 退出系统
                print('您已退出学生成绩管理系统！')
                ctrl = False
            elif option_str == '1':  # 录入学生成绩信息
                insert()
            elif option_str == '2':  # 查找学生成绩信息
                search()
            elif option_str == '3':  # 删除学生成绩信息
                delete()
            elif option_str == '4':  # 修改学生成绩信息
                modify()
            elif option_str == '5':  # 排序
                sort()
            elif option_str == '6':  # 统计学生总数
                total()
            elif option_str == '7':  # 显示所有学生信息
                show()


'''1 录入学生信息'''


def insert():
    stdentList = []        # 保存学生信息的列表
    mark = True  # 是否继续添加
    while mark:
        id = input("请输入ID（如 1001）：")
        if not id:  # ID为空，跳出循环
            break
        name = input("请输入名字：")
        if not name:  # 名字为空，跳出循环
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效，不是整型数值．．．．重新录入信息")
            continue
        stdent = {"id": id, "name": name, "english": english, "python": python, "c": c}  # 将输入的学生信息保存到字典
        stdentList.append(stdent)  # 将学生字典添加到列表中
        inputMark = input("是否继续添加？（y/n）:")
        if inputMark == "y":  # 继续添加
            mark = True
        else:  # 不继续添加
            mark = False
    save(stdentList)  # 将学生信息保存到文件
    print("学生信息录入完毕！！！")


# 将学生信息保存到文件
def save(student):
    try:
        students_txt = open(filename, "a")  # 以追加模式打开
    except Exception as e:
        students_txt = open(filename, "w")  # 文件不存在，创建文件并打开
    for info in student:
        students_txt.write(str(info) + "\n")  # 按行存储，添加换行符
    students_txt.close()  # 关闭文件


'''2 查找学生成绩信息'''


def search():
    mark = True
    student_query = []  # 保存查询结果的学生列表
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):  # 判断文件是否存在
            mode = input("按ID查输入1；按姓名查输入2：")
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入！")
                continue  # 重新查询
            with open(filename) as file:  # 打开文件
                student = file.readlines()  # 读取全部内容
                for list in student:
                    d = dict(eval(list))  # 字符串转字典
                    if id is not "":  # 判断是否按ID查
                        if d['id'] == id:
                            student_query.append(d)  # 将找到的学生信息保存到列表中
                    elif name is not "":  # 判断是否按姓名查
                        if d['name'] == name:
                            student_query.append(d)  # 将找到的学生信息保存到列表中
                show_student(student_query)  # 显示查询结果
                student_query.clear()  # 清空列表
                inputMark = input("是否继续查询？（y/n）:")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息...")
            return


'''3 删除学生成绩信息'''


def delete():
    mark = True  # 标记是否循环
    while mark:
        studentId = input("请输入要删除的学生ID：")
        if studentId is not "":  # 判断要删除的学生是否存在
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r') as rfile:  # 打开文件
                    student_old = rfile.readlines()  # 读取全部内容
            else:
                student_old = []
            ifdel = False  # 标记是否删除
            if student_old:  # 如果存在学生信息
                with open(filename, 'w') as wfile:  # 以写方式打开文件
                    d = {}  # 定义空字典
                    for list in student_old:
                        d = dict(eval(list))  # 字符串转字典
                        if d['id'] != studentId:
                            wfile.write(str(d) + "\n")  # 将一条学生信息写入文件
                        else:
                            ifdel = True  # 标记已经删除
                    if ifdel:
                        print("ID为 %s 的学生信息已经被删除..." % studentId)
                    else:
                        print("没有找到ID为 %s 的学生信息..." % studentId)
            else:  # 不存在学生信息
                print("无学生信息...")
                break  # 退出循环
            show()  # 显示全部学生信息
            inputMark = input("是否继续删除？（y/n）:")
            if inputMark == "y":
                mark = True  # 继续删除
            else:
                mark = False  # 退出删除学生信息功能


'''4 修改学生成绩信息'''


def modify():
    show()  # 显示全部学生信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
    else:
        return
    studentid = input("请输入要修改的学生ID：")
    with open(filename, "w") as wfile:  # 以写模式打开文件
        for student in student_old:
            d = dict(eval(student))  # 字符串转字典
            if d["id"] == studentid:  # 是否为要修改的学生
                print("找到了这名学生，可以修改他的信息！")
                while True:  # 输入要修改的信息
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入Python成绩："))
                        d["c"] = int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入。")
                    else:
                        break  # 跳出循环
                student = str(d)  # 将字典转换为字符串
                wfile.write(student + "\n")   # 将修改的信息写入到文件
                print("修改成功！")
            else:
                wfile.write(student)  # 将未修改的信息写入到文件
    mark = input("是否继续修改其他学生信息？（y/n）：")
    if mark == "y":
        modify()  # 重新执行修改操作


'''5 排序'''


def sort():
    show()  # 显示全部学生信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as file:  # 打开文件
            student_old = file.readlines()  # 读取全部内容
            student_new = []
        for list in student_old:
            d = dict(eval(list))  # 字符串转字典
            student_new.append(d)  # 将转换后的字典添加到列表中
    else:
        return
    ascORdesc = input("请选择（0升序；1降序）：")
    if ascORdesc == "0":  # 按升序排序
        ascORdescBool = False           # 标记变量，为False表示升序排序
    elif ascORdesc == "1":  # 按降序排序
        ascORdescBool = True          # 标记变量，为True表示降序排序
    else:
        print("您的输入有误，请重新输入！")
        sort()  
    mode = input("请选择排序方式（1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；0按总成绩排序）：")
    if mode == "1":  # 按英语成绩排序
        student_new.sort(key=lambda x: x["english"], reverse=ascORdescBool)
    elif mode == "2":  # 按Python成绩排序
        student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
    elif mode == "3":  # 按C语言成绩排序
        student_new.sort(key=lambda x: x["c"], reverse=ascORdescBool)
    elif mode == "0":  # 按总成绩排序
        student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=ascORdescBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_new)  # 显示排序结果


''' 6 统计学生总数'''


def total():
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
            if student_old:
                print("一共有 %d 名学生！" % len(student_old))
            else:
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息...")


''' 7 显示所有学生信息 '''


def show():
    student_new = []
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
        for list in student_old:
            student_new.append(eval(list))  # 将找到的学生信息保存到列表中
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息...")


# 将保存在列表中的学生信息显示出来
def show_student(studentList):
    if not studentList:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"), info.get("name"), str(info.get("english")), str(info.get("python")),
                                 str(info.get("c")),
                                 str(info.get("english") + info.get("python") + info.get("c")).center(12)))


if __name__ == "__main__":
    main()
