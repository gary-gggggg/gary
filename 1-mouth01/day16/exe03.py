"""练习 1：使用生成器表达式在列表中获取所有字符串.
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
练习 2：在列表中获取所有整数,并计算它的平fang."""
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]

gd1 = (item for item in list01 if type(item) is str)
for item in gd1:
    print(item)

gd2 = (item2 for item2 in list01 if type(item2) is int)
for item2 in gd2:
    result=item2**2
    print(result)



