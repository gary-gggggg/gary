class V1:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴做表是{self.x}，Y轴坐标是{self.y}。"

    def __imul__(self, other):
        if type(other) == V1:
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self


p1 = V1(12, 9)
p2 = V1(7, 13)
p1*=p2
p1*=p2
p1*=p2
p1*=p2
p1*=p2
p1*=p2
p1*=p2
p1*=p2
p1*=p2
p1*=p2
print(p1)
