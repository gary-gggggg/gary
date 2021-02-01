"""练习 1：创建列表,使用迭代思想,打印每个元素. 练习
2：创建字典,使用迭代思想,打印每个键值对"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iterator = list1.__iter__()
while 1:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
dic = {"giao": "giao1", "fiao": "fiao1", "xiao": "xiao1"}
iterator1 = dic.__iter__()
while 1:
    try:
        key1 = iterator1.__next__()
        print(key1,dic[key1])
    except StopIteration:
        break
