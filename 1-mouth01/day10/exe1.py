"""练习 1：创建狗类数据：品种、昵称、身长、体重
行为：吃(体重增长 1)
实例化两个对象并调用其函数画出内"""


class Dog:
    def __init__(self, race=None, weight=0, name="", longth=0):
        self.race = race
        self.weight = weight
        self.name = name
        self.longth = longth

    def eating(self):
        print("啃")
        self.weight += 1
keven=Dog("土狗",10,"keven",20)
keven.eating()
keven.eating()
keven.eating()
print(keven.weight)
giao=Dog("皮狗",125,"giao",30)
giao.eating()
giao.eating()
print(giao.weight)

