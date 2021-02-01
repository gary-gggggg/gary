 """6.列表推导式：
  计算1970年到2050年之间所有闰年"""
sum=[]
for i in range(1970,2051):
    if i%4==0 and i%100!=0:
        sum.append(i)
print(sum)