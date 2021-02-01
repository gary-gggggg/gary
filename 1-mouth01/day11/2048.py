"""4. (选做)面向过程 2048游戏核心算法
list_merge = [2,0,0,2]
(1). 定义函数,零元素移动到末尾
     [2,0,0,2]  -->   [2,2,0,0]
     [2,0,2,0]  -->   [2,2,0,0]
     [2,0,4,2]  -->   [2,4,2,0]
(2). 定义函数,相邻相同数字合并
     [2,0,0,2]-调用函数1->[2,2,0,0]->[4,0,0,0]
     [2,0,2,0]-调用函数1->[2,2,0,0]->[4,0,0,0]
     [8,8,8,8]        -->           [16,16,0,0]
     [8,8,8,0]        -->           [16,8,0,0]
"""
listz = [[2, 0, 2, 0], [2, 0, 0, 2], [4, 2, 0, 2], [2, 2, 2, 2]]

def left(gg):
    giao = 0
    for i in gg:
        for i2 in i:
            if i2==giao:
                i.remove(giao)
                i.insert(len(i) + 1, giao)

left(listz)
print(listz)#[[2, 2, 0, 0], [2, 2, 0, 0], [4, 2, 2, 0], [2, 2, 2, 2]]

listg=[[2, 2, 0, 0], [2, 2, 0, 0], [4, 2, 2, 0], [2, 2, 2, 2]]

def gathering(ggg):
    while 1:
        for i3 in ggg:
            for c in range(len(i3)-1):
                for c1 in range(c+1,len(i3)):
                    if i3[c]==i3[c1]:
                        i3[c]=i3[c]+i3[c1]
                        del i3[c1]
                        i3.append(0)
                        left(ggg)

gathering(listz)
print(listz)
