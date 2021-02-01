from real.model import EmployeeModel


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
        em1=EmployeeModel(em=number_em)
        if em1 in self.__employee_list:
            self.__employee_list.remove(em1)
            return True
        return False

    def update_einfo(self, em1):
        for i in self.__employee_list:
            if i.em==em1.em:
                i.__dict__=em1.__dict__
                return True
            return False
