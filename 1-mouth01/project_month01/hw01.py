"""1. 员工信息管理系统
    添加/显示/删除/修改"""


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0, em=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money
        self.em = em

    def __str__(self):
        return f"{self.name}的员工编号是{self.eid}，部门编号是{self.did}，工资是{self.money}，员工识别码是{self.em}"

    def __eq__(self, other):
        return self.em == other.em


class EmployeeView:
    def __init__(self):
        self.controller = EmployeeController()

    def __display_menu(self):
        print("输入1输入员工信息：")
        print("输入2显示员工信息：")
        print("输入3删除员工信息：")
        print("输入4修改员工信息：")

    def __select_menu(self):
        giao1 = int(input("请输入数字："))
        if giao1 == 1:
            self.input_einfo()
        elif giao1 == 2:
            self.show_the_info()
        elif giao1 == 3:
            self.remove_info()
        elif giao1 == 4:
            self.update_info()
        else:
            self.qita()

    def input_einfo(self):
        eem = EmployeeModel()
        eem.eid = input("请输入员工编号：")
        eem.did = input("请输入部门编号：")
        eem.name = input("请输入员工姓名：")
        eem.money = input("请输入员工工资：")
        self.controller.input_einfo(eem)
        print("添加成功")

    def show_the_info(self):
        for i in self.controller.employee_list:
            print(i)

    def main(self):
        while 1:
            self.__display_menu()
            self.__select_menu()

    def remove_info(self):
        number_em = int(input("请输入您需要删除的员工识别码："))
        if self.controller.remove_einfo(number_em):
            print("删除成功")
        else:
            print("删除失败")

    def update_info(self):
        eem = EmployeeModel()
        eem.em = int(input("请输入您要的员工的识别码："))
        eem.eid = input("请输入员工编号：")
        eem.did = input("请输入部门编号：")
        eem.name = input("请输入员工姓名：")
        eem.money = input("请输入员工工资：")
        if self.controller.update_einfo(eem):
            print("修改成功")
        else:
            print("修改失败")

    def qita(self):
        print("输入错误")


class EmployeeController:
    def __init__(self):
        self.__employee_list = []
        self.em_number = 100

    @property
    def employee_list(self):
        return self.__employee_list

    def input_einfo(self, eem):
        eem.em = self.em_number
        self.em_number += 1
        self.__employee_list.append(eem)

    def remove_einfo(self, number_em):
        em1 = EmployeeModel(em=number_em)
        if em1 in self.__employee_list:
            self.__employee_list.remove(em1)
            return True
        return False

    def update_einfo(self, em1):
        for i in self.__employee_list:
            if i.em == em1.em:
                i.__dict__ = em1.__dict__
                return True
            return False


giaog = EmployeeView()
giaog.main()
