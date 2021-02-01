"""张无忌教赵敏九阳神功
赵敏教张无忌玉女心经
张无忌工作挣了5000元
赵敏工作挣了10000元"""


class Person:
    def __init__(self, name=""):
        self.name=name
    def skill(self,student,kongfu):
        print(f"{self.name}教{student}{kongfu}")
    def work(self,money):
        print(f"{self.name}工作挣了{money}元")

zwj=Person("")
zm=Person("")
zwj.skill("赵敏","九阳神功")
zm.skill("张无忌","玉女心经")
zwj.work(5000)
zm.work(10000)

