"""3. 以面向对象的思想,描述下列情景.
   (1)需求：小明使用手机打电话
   (2)小明一次请多个保洁打扫卫生
      效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
   (3)张无忌教赵敏九阳神功
   赵敏教张无忌玉女心经
   张无忌工作挣了5000元
   赵敏工作挣了10000元
"""


class Person:
    def __init__(self, name=""):
        self.name = name
        self.__tolll = Tool()

    def using(self):
        print("使用")
        self.__tolll.calling()


class Tool:
    def __init__(self, phone=""):
        self.phone = phone

    def calling(self):
        print("打电话")


xm1 = Person("小明")
t1 = Tool("华为")
xm1.using()
