"""输入多人身高，若输入空字符则停止，在得出平均值"""
sum=0
sum1=0
while True:
   hight=input("请输入您的身高：")
   if hight==" ":
       break
   hight1=int(hight)
   sum+=hight1
   sum1+=1
print(sum/sum1)



