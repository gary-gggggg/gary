"""练习1：输入5人身高，算出平均值"""
# sum=0
# sum1=0
# while True:
#     hight=int(input("请输入您的身高："))
#     sum+=hight
#     sum1+=1
#     if sum1==5:
#         break
# print(sum/5)

sum=0
for i in range(4):
    sum+=int(input("身高："))
print(sum/i)
