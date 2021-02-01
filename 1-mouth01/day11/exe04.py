"""
玩家
"""


class Player:
    def __init__(self, atk):
        self.atk = atk

    def atking(self, enemy):
        print("攻击")
        enemy.demaged(self.atk)


class Enemy:
    def __init__(self, hp):
        self.hp = hp

    def demaged(self,value):
        self.hp-=value
        print("受伤,还剩",self.hp)

p1 = Player(55)
e1=Enemy(100)
p1.atking(e1)
p1.atking(e1)
