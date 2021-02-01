"""
    需求:
        创建员工管理器
        -- 存储很多员工
        -- 计算所有员工总薪资
    岗位:
        程序员:底薪 + 项目分红
        测试员:底薪 + Bug数*5元
    要求:
        增加新岗位,员工管理器不变.
    设计:
        封装(分):创建员工管理器类/程序员类/测试员类
        继承(隔):创建岗位类,隔离员工管理器类与具体岗位(程序员类/测试员类)与的变化
        多态(做):具体岗位(程序员类/测试员类)重写岗位类的计算薪资方法,以实现具体功能
"""


class StaffAdministrator:
    def __init__(self):
        self.__n_staff = []

    def calculate_sum_wage(self):
        tt_wage = 0
        for i in self.__n_staff:
            tt_wage += i.calculate_wage()
            return tt_wage

    def add_staff(self, emp):
        self.__n_staff.append(emp)


class Position:
    def calculate_wage(self):
        pass


class Programmer(Position):
    def calculate_wage(self):
