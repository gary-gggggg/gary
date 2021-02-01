"""练习 1：以面向对象思想，描述下列情景：
情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)
变化：还可能伤害房子、树、鸭子....
要求：增加新事物，不影响手雷.
画出架构设"""


class Victim:
    def __init__(self, name=None):
        self.name=name


class Graned(Victim):
    def __init__(self, name=None):
        super().__init__(name)
    def explode(self):
        print("爆炸")

    def __str__(self):


class Enemy:
    def demage(self):
        print("爆头")

p1= Victim()
print(p1)
