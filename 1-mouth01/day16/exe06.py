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


def edis(n):
    return n.eid and n.money


def select(kdddx, n):
    for item in kdddx:
        if n(item):
            yield n(item)


for name in select(list_employees, lambda g: g.name):
    print(name)



