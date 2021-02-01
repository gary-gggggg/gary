# list=[1,23,465,132,456,132,4,3,1,654,61,6,4789,74,61]
# list.sort(reverse=True)
# print(list)
"""对数字列表进行升序排列（大 --> 小）"""
list1=[23,465,132,456,132,4,3,1,654,61,6,4789,74,61]
for r1 in range(len(list1)-1):
    for r2 in range(r1+1,len(list1)):
        if list1[r1] < list1[r2]:
            list1[r1],list1[r2]=list1[r2],list1[r1]
print(list1)


