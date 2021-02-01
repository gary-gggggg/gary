"""练习：
直接打印商品对象: xx 的编号是 xx,单价是 xx
直接打印敌人对象: xx 的攻击力是 xx,血量是 """


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.cid}的编号是{self.name},单价是{self.price}津巴布韦币"


class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp =hp

    def __str__(self):
        return f"{self.name}的攻击力是{self.atk},血量是{self.hp}"

p1=Commodity("giao",41654,45114564645664)
e1=Enemy("FIAO",789453,789494684)
print(p1)
print(e1)
