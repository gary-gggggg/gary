class MyRange:
    def __init__(self, n):
        self.n = n
        self.mynubmer = []

    def add_number(self):
        self.n -= 1
        self.mynubmer.append(n)

    def __iter__(self):
        return Myrangeiterator(self.mynubmer)


class Myrangeiterator:
    def __init__(self, nn):
        self.nn = nn
        self.mg = MyRange

    def __next__(self):
        if len(self.nn)>self.mg.n:
            raise StopIteration
        return self.mg.n


for number in MyRange(5):
    print(number)  # 0 1 2 3
