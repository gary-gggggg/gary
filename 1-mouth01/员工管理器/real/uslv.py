from real.model import EmployeeModel
from real.scc import EmployeeController


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

    def __get_number(self, nn):
        while 1:
            try:
                number = int(input(nn))
                return number
            except:
                print("输入格式不对！")

    def input_einfo(self):
        eem = EmployeeModel()
        eem.eid = self.__get_number("请输入员工编号：")
        eem.did = self.__get_number("请输入部门编号：")
        eem.name = input("请输入员工姓名：")
        eem.money = self.__get_number("请输入员工工资：")
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
        number_em = self.__get_number("请输入您需要删除的员工识别码：")
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
