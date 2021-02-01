class V1:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴做表是{self.x}，Y轴坐标是{self.y}。"

    def __sub__(self, other):
        if type(other) == V1:
            x = self.x - other.x
            y = self.y - other.y
        else:
            x = self.x - other
            y = self.y - other
        return V1(x, y)


p1 = V1(12, 17)
p2 = V1(2, 3)
p3 = p1 - p2
p4 = p1 - 10
print(p3)
print(p4)
