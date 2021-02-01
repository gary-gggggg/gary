
class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0, em=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money
        self.em = em

    def __str__(self):
        return f"{self.name}的员工编号是{self.eid}，部门编号是{self.did}，工资是{self.money}，员工识别码是{self.em}"

    def __eq__(self,other):
        return self.em==other.em