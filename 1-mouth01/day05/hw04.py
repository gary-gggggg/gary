"""在终端中录入疫情地区名称，如果输入空字符串，则停止。
   最后倒序打印所有地区名称(一行一个)
   要求：录入的名称已经存在不要再次添加.
   提示： in """
sum=[]
while 1:
    region=input("输入疫情地区：")
    if region=="":
        break
    if region in sum:
        print("录入的名称已经存在不要再次添加")
        continue
    sum.append(region)
for i in sum[::-1]:
    print(i)
