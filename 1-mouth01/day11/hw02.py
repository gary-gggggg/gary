"""3. 以面向对象的思想,描述下列情景.
   (1)需求：小明使用手机打电话
   (2)小明一次请多个保洁打扫卫生
      效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
   (3)张无忌教赵敏九阳神功
   赵敏教张无忌玉女心经
   张无忌工作挣了5000元
   赵敏工作挣了10000元
"""


class Client:
    def __init__(self, members, name=""):
        self.name = name
        self.members=members

    def info(self):
        print("通知")
        for i in range(self.members):
            clean=Worker()
            clean.cleaning()

class Worker:
    def cleaning(self):
        print("打扫卫生")

real_one=Client(12,"小明")
real_one.info()

