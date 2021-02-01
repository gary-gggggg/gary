"""面向对象
   创建桌子类
        数据：品牌,材质,尺寸(长,宽,高)
   创建电脑类
        数据:型号,CPU型号,内存大小,硬盘大小
        行为：开机,关机"""


class Desk:
    def __init__(self, brand, material, size=(0, 0, 0)):
        self.brand = brand
        self.material = material
        self.size = size


class Computer:
    def __init__(self, type_computer, cpu_type, memory, hard_disk):
        self.type_computer = type_computer
        self.cpu_type = cpu_type
        self.memory = memory
        self.hard_disk = hard_disk

    def turning_on(self):
        print(self.type_computer + "开机")

    def turing_off(self):
        print(self.type_computer + "关机")


xxt = Computer("sad", "giao","dde", "qpirf")
print(xxt.type_computer)
xxt.turing_off()
xxt.turning_on()