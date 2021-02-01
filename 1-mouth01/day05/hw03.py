""" 计算列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
    字符串列表：words =["qtx","看一看","想啊想","练练"]
    结果:2"""
words =["qtx","看一看","想啊想","练练"]
sum=0
for i in words:
    if len(i)>2 and i[0]==i[-1]:
        sum+=1
print(sum)

