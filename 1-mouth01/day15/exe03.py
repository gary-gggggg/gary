"""练习 1：遍历商品控制器"""


class Graphiciterator:
    def __init__(self, date):
        self.date = date
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index > len(self.date) - 1:
            raise StopIteration
        return self.date[self.index]


class GraphicController:
    def __init__(self):
        self.__list_graphic = []

    def add_graphic(self, graphic):
        self.__list_graphic.append(graphic)

    def __iter__(self):
        return Graphiciterator(self.__list_graphic)


controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
