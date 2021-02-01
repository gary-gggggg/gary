"""range累加"""
n=int(input("请输入开始数："))
n2=int(input("请输入结束数+-1："))
n3=int(input("请输入间隔数："))
sum=0
for i in range(n,n2,n3):
    sum+=i
print(sum)