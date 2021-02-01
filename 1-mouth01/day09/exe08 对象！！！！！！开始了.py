"""变量 = 类名(参数列表)
练习：创建手机类
数据：品牌、价格、颜色
行为：通话实例化两个对象并调用其函数
画出内图"""


class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def calling(self):
        print(self.brand + "通话")


iphone = Phone("苹果", 8999, "金")
xiaomi = Phone("小米", 6777, "红")
print(iphone.brand)
print(xiaomi.color)
iphone.calling()
