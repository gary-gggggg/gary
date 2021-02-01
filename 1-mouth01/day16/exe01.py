"""练习 1：将列表中所有奇数设置为 None练习
2：将列表中所有偶数自增1"""
list1=[1,2,64,9,31,96745,4,451,67]
for i, item in enumerate(list1):
    if item%2!=0:
        list1[i]=None
print(list1)

list2=[1,2,64,9,31,96745,4,4512,672]
for i1, element in enumerate(list2):
    if element%2==0:
        list2[i1]+=1
print(list2)
