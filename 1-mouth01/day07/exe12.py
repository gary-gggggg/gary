"""练习 2：创建函数,在终端中打印矩形. \
number = int(input("请输入整数:"))
# 5for row in range(number):
if row == 0 or row == number - 1:
print("*" * number)
else: print("*%s*" % (" " * (number - 2)"""
# number = int(input("请输入整数:"))
# for row in range(number):
#     if row == 0 or row == number - 1:
#         print("*" * number)
#     else:
#         print("*%s*" % (" " * (number - 2)))

def print_re(number):
    for row in range(number):
        if row == 0 or row == number - 1:
             print("*" * number)
        else:
             print("*%s*" % (" " * (number - 2)))
print_re(5)