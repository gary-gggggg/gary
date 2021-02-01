"""练习 2：二维列表
list01 = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
]
1. 将第一行从左到右逐行打印
效果：1
2
3
4
5
2. 将第二行从右到左逐行打印
效果：10
9
8
7
6
3. 将第三列行从上到下逐个打印
效果：3
8
13
4. 将第四列行从下到上逐个打印
效果：14
9
4
5. 将二维列表以表格状打印
效果：1 2 3 4 5
6 7 8 9 10
11 12 13 14 15"""
list01 = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
]
for l in list01[0]:
    print(l)
# for l1 in list01[1][::-1]:
#     print(l1)
for l1 in range(len(list01[0])-1,-1,-1):
    print(list01[1][int(l1)])
for l3 in list01:
    print(l3[2])
# for l4 in list01[::-1]:
#     print(l4[3])
for l4 in range(len(list01)-1,-1,-1):
    # print(l4)
    print(list01[l4][3])
for l5 in list01:
    for l6 in l5:
        print(l6,end=" ")
    print()
