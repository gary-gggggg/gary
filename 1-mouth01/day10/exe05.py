"""练习 1：创建敌人类，
并保护数据在有效范围内数据:姓名/ 攻击力/ 血量
                            0-100 0-500
"""


class Enemy:
    def __init__(self, name, atk=None, hp=None):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 < value < 100:
            self.__atk = value
        else:
            raise exception("去你妈的")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 < value < 500:
            self.__hp = value
        else:
            raise exception("滚你妈的")


m1 = Enemy("giao", 99, 499)
print(m1.name)
