"""练习 4：定义函数，将列表中大于某个值的元素设置为 None
参数                                 结果
[34, 545, 56, 7, 78, 8] -10-> [None,None,None,7,None,8]
[34, 545, 56, 7, 78, 8] -100-> [34, None, 56, 7, 78, 8]"""
def number_gt(l1,n1):
    for i in range(len(l1)):
        if l1[i]>n1:
            l1[i]=None

a=[34, 545, 56, 7, 78, 8]
b=[34, 545, 56, 7, 78, 8]
number_gt(a,10)
print(a)

