"""在终端中输入任意个数的数字，然后将其转化陈unicode的形式
若是输入空字符串则终止循环"""
while True:
    number = input("请输入一个数字：")
    if number == (""):
        break
    number1 = int(number)
    result = chr(number1)
    print(result)
