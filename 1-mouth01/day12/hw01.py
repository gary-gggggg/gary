"""
    (1). 根据格式打印老婆对象:xx的身高是xx,颜值是xx.
        效果：print(Wife("双儿", 170, 98))
             双儿的身高是170,颜值是98.
    (2). 判断阿珂是否在列表中 Wife("阿珂") in list_wife
    (3). 计算苏荃在列表中存在的个数list_wife.count(Wife("苏荃"))
    (4). 查找颜值最高的老婆对象max(list_wife)
    (5). 根据颜值对老婆列表进行升序排列list_wife.sort()"""


class Wife:
    def __init__(self, name="", height=0, face_score=0):
        self.name = name
        self.height = height
        self.face_score = face_score

    def __str__(self):
        return f"{self.name}的身高是{self.height},颜值是{self.face_score}"

    def __eq__(self, other):
        return self.name == other
    def __gt__(self, other):
        return self.face_score<other




list_wife = [
    Wife("双儿", 170, 98),
    Wife("阿珂", 173, 100),
    Wife("苏荃", 160, 99),
    Wife("丽丽", 167, 90),
    Wife("芳芳", 168, 92),
    Wife("苏荃", 160, 99), ]

print(Wife("双儿", 170, 98))  # 1
print(Wife("giao") in list_wife)#2
print(list_wife.count(Wife("苏荃")))#3
print(max(list_wife))#4
list_wife.sort()
print(list_wife)


