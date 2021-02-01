"""练习 2：
创建图形管理器
1. 记录多种图形（圆形、矩形....）
2. 提供计算总面积的方法.
满足：开闭原则测试：
创建图形管理器，存储多个图形对象。
通过图形管理器，调用计算总面积方法"""


class Calculater:  # 开闭原则
    def __init__(self):
        self.__all_shape = []  # 组合复用

    def tt_areas(self):
        tta = 0
        for i in self.__all_shape:
            tta += i.calculate_area()
            return tta

    def add_shape(self, shape):
        if isinstance(shape, Calculate_area1):  # 依赖倒置
            self.__all_shape.append(shape)  # 迪米特法则


class Calculate_area1:  # 依赖倒置
    def calculate_area(self):
        pass


class Circle(Calculate_area1):  # 里氏替换
    def __init__(self, r=0):
        self.r = r

    def calculate_area(self):  # 类的单一职责
        super().calculate_area()
        return self.r ** 2 * 3.14159265758


class rectangle(Calculate_area1):
    def __init__(self, lonth=0, width=0):
        self.lonth = lonth
        self.width = width

    def calculate_area(self):
        super().calculate_area()
        return self.lonth * self.width


s1 = Calculater()
s1.add_shape(Circle(456496))
s1.add_shape(rectangle(165,4564654))

