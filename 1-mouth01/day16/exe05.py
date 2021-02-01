"""练习 2：需求：
定义函数，在员工列表中查找编号是 1003 的员工
定义函数，在员工列表中查找姓名是孙悟空的员工"""
from gongju.gongjuren import Iterablehelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.did = did
        self.eid = eid
        self.name = name
        self.money = money


list_employees = [Employee(1001, 9002, "师父", 60000),
                  Employee(1002, 9001, "孙悟空", 50000),
                  Employee(1003, 9002, "猪八戒", 20000),
                  Employee(1004, 9001, "沙僧", 30000),
                  Employee(1005, 9001, "小白龙", 15000)]

print(Iterablehelper.find_singel01(list_employees, lambda giao: giao.name == "孙悟空").__dict__)
print(Iterablehelper.find_singel01(list_employees, lambda giao: giao.eid == 1003).__dict__)
