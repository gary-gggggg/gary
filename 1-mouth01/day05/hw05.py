"""在终端中录入5个疫情省份的确诊人数
   最后打印最大值、最小值、平均值.
   （使用内置函数实现）"""
sum1=[]
for i in range(5):
    sum1.append(int(input("请输入人数：")))
print(f"{max(sum1)},{min(sum1)},{sum(sum1)/len(sum1)}")