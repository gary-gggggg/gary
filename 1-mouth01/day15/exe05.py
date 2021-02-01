class MyRangeIterator:
    def __init__(self, begin_num, end_num=0):
        self.end_num = end_num
        self.begin_num = begin_num
        self.num = self.begin_num -1

    def __next__(self):
        self.num += 1
        if self.num > self.end_num:
            raise StopIteration
        return self.num


class MyRange:
    def __init__(self, begin_num, end_num=0):
        self.begin_num = begin_num
        self.end_num = end_num

    def __iter__(self):
        return MyRangeIterator(self.begin_num,self.end_num)


for i in MyRange(5, 20):
    print(i)
