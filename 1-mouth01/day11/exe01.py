"""
技能，读写
桌子，只读
"""


class Skill:
    def __init__(self, cdr=None, atk=None, mp=None):
        self.cdr = cdr
        self.atk = atk
        self.mp = mp

    @property
    def cdr(self):
        return self.__cdr

    @cdr.setter
    def cdr(self, value):
        if 0 < value < 120:
            self.__cdr = value
        else:
            raise Exception("冷却不行啊弟弟")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 < value < 200:
            self.__atk = value
        else:
            raise Exception("攻击理不行啊弟弟")

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, value):
        if value == 100:
            self.__mp = value
        else:
            raise Exception("法力不行弟弟")


giao = Skill(85, 120, 100)
print(giao.mp)


class Desk:
    def __init__(self):
        self.__brand = "giao"
        self.__material = "纸"
        self.__size =(120,450,610)

    @property
    def brand(self):
        return self.__brand

    @property
    def material(self):
        return self.__material

    @property
    def size(self):
        return self.__size


m2 = Desk()
print(m2.brand)
print(m2.__dict__)
