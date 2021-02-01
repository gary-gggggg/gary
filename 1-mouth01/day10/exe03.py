"""

"""


class Myclass:
    d2 = 1
    def __init__(self):
        self.d1 = 1
        self.d1 += 1
        Myclass.d2 += 1


m1 = Myclass()
m2 = Myclass()
m3 = Myclass()
print(m3.d1)
print(Myclass.d2)
