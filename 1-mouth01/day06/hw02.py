"""4. 将列表中整数的十位不是3和7和8的数字存入另外一个列表
   list03 = [135, 63, 227, 675, 470, 733, 3127]
   结果:[63, 227, 3127]"""
# list03 = [135, 63, 227, 675, 470, 733, 3127]
# sum=[]
# for i in range(len(list03)):
#     sum.append(str(list03[i]))
# print(sum) #['135', '63', '227', '675', '470', '733', '3127']
# res1=[]
# x=""
# x1=""
# for l in sum:
#     x=l
#     x1=x[len(x)-2]
#     if "3" in x1 or "7" in x1 or "8" in x1:
#         continue
#     res1.append(x)
# print(res1)
list03 = [135, 63, 227, 675, 470, 733, 3127]
suv=[]
for i in list03:
    u=str(i)[-2]
    if u in ("3","7","8"):
        continue
    suv.append(i)
print(suv)