"""练习：创建父类：车(品牌，速度)
创建子类：电动车(电池容量,充电功率)
创建子类对象并画出内存图"""
class Car:
    def __init__(self, brand=None, speed=None):
        self.brand=brand
        self.speed=speed

class ECar(Car):
    def __init__(self,brand=None, speed=None,balerry=None, charge_speed=None):
        super().__init__(brand,speed)
        self.balerry=balerry
        self.charge_speed=charge_speed

c1=ECar("tesla","100/h","100%","500kw/h")
print(c1.brand)
