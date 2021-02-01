"""输入3个整数，请把这3个数从小到大输出成列表"""
# x = int(input("输入："))
# y = int(input("输入："))
# z = int(input("输入："))
# if x > y:
#     x, y = y, x
# if x > z:
#        x, z = z, x
# if y > z:
#     y, z = z, y
# res.append(x)
# res.append(y)
# res.append(z)
res = []
for i in range(3):
    res.append(input("输入："))
res.sort()
print(res)