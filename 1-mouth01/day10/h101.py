""" 使用封装数据的思想
   创建员工类/部门类,修改实现下列功能.
    1. 定义函数,打印所有员工信息,
    格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    2. 定义函数,打印所有月薪大于2w的员工信息,
    格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    3. 定义函数,打印所有员工的部门信息,
    格式：xx的部门是xx,月薪xx元.
    4. 定义函数,查找薪资最少的员工
    5. 定义函数,根据薪资对员工列表升序排列

    # 员工列表
    list_employees = [
        {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
        {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
        {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
        {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
        {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
    ]

    # 部门列表
    list_departments = [
        {"did": 9001, "title": "教学部"},
        {"did": 9002, "title": "销售部"},
    ]
"""


class Emplyee:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


class Departments:
    def __init__(self, did=0, title=""):
        self.did = did
        self.title = title


def print_detail(i):
    print(f"{i.name}的员工编号是{i.eid},部门编号是{i.did},月薪{i.money}元")


list_employees = [
    Emplyee(1001, 9002, "师父", 60000),
    Emplyee(1002, 9001, "孙悟空", 50000),
    Emplyee(1003, 9002, "猪八戒", 20000),
    Emplyee(1004, 9001, "沙僧", 30000),
    Emplyee(1005, 9001, "小白龙", 15000), ]

list_departments = [Departments(9001, "教学部"),
                    Departments(9002, "销售部"), ]


def print_all_member():
    for i in list_employees:
        print_detail(i)


print_all_member()  # 1

def print_salary_2w():
    for i in list_employees:
        if i.money > 20000:
            print_detail(i)


print_salary_2w()#2

def print_all_eandd_infp():
    for l in list_employees:
        for l2 in list_departments:
            if l.did == l2.did:
                l.did = l2.title
                print(f"{l.name}的部门是{l.did},月薪{l.money}元.")


print_all_eandd_infp()  # 3

def find_mallist_wage():
    min1_wage = list_employees[0]
    for c in range(len(list_employees)):
        for c1 in range(1,len(list_employees)):
            if min1_wage.money>list_employees[c1].money:
                min1_wage=list_employees[c1]
    print(min1_wage.name)


find_mallist_wage()#4

def descending_list():
    for c2 in range(len(list_employees)-1):
        for c3 in range(c2+1,len(list_employees)):
            if list_employees[c2].money>list_employees[c3].money:
                list_employees[c2].money,list_employees[c3].money=list_employees[c3].money,list_employees[c2].money

descending_list()
for k in list_employees:#5
    print_detail(k)





