""" 需求：
        定义函数，在员工列表中查找所有薪资大于20000的员工数量
        定义函数，在员工列表中查找所有部门编号是9001的员工数量
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数get_count(定义到单独模块中)
        3. 在当前模块中调用(使用lambda)
4. 需求：
        定义函数，在员工列表中查找员工编号最小的员工
        定义函数，在员工列表中查找薪资最少的员工
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数get_min(定义到单独模块中)
        3. 在当前模块中调用(使用lambda)
5. 需求：
        定义函数，根据薪资对员工列表进行升序排列
        定义函数，根据员工编号对员工列表进行升序排列
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数order_by(定义到单独模块中)
        3. 在当前模块中调用(使用lambda)
class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money"""
from gongjuren import Iterablehelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

print(Iterablehelper.find_count(list_employees, lambda q: q.money > 20000))
print(Iterablehelper.find_count(list_employees, lambda q: q.did == 9001))#1

print(Iterablehelper.find_min(list_employees, lambda g: g.eid))
print(Iterablehelper.find_min(list_employees, lambda m: m.money))  # 2

for t3 in Iterablehelper.order_by(list_employees, lambda m1: m1.money):
    print(t3.__dict__)

for t4 in Iterablehelper.order_by(list_employees, lambda m2: m2.eid):
    print(t4.__dict__)
