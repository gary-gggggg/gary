"""(选做)定义函数,将列表中奇数删除
   测试数据:[3,7,5,6,7,8,9,13] --> [6,8]
   提示:在列表中删除多个元素,倒序删除"""


def giao(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 1:
            del l[i]


list = [3, 7, 5, 6, 7, 8, 9, 13]
result = giao(list)
print(list)
