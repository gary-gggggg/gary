"""创建函数,打印所有员工信息
   创建函数,打印所有月薪大于2w的员工信息,
   创建函数,在部门列表中查找编号最小的部门
   创建函数,根据部门编号对部门列表升序排列"""

# 员工列表(员工编号 部门编号 姓名 工资)
dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

# 部门列表
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]


def giao1():
    for k, v in dict_employees.items():
        return f"{v['name']}的员工编号是{k},部门编号是{v['d']},月薪{v['money']}元"


def giao2():
    for k, v in dict_employees.items():
        if int(v["money"]) > 20000:
        return f"{v['name']}的员工编号是{k},部门编号是{v['did']},月薪{v['money']}元"

def giao3():
    minn = list_departments[0]["did"]
    for c in range(1, len(list_departments)):
        if minn > list_departments[c]["did"]:
            c = minn
    return minn

def giao4():
    minn = list_departments[0]["did"]
    for c in range(1, len(list_departments)):
        if minn > list_departments[c]["did"]:
            c = minn
    return minn

giao1()
giao2()
giao3()
giao4()
