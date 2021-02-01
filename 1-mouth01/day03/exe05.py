"""在终端中录入 4 个同学身高,打印最高的值.
算法：170 160 180  165假设第一个就是最大值使用假设的和第二个进行比较,
发现更大的就替换假设的使用假设的和第三个进行比较,
发现更大的就替换假设的使用假设的和第四个进行比较,
发现更大的就替换假设的最后假设的就是最大的"""
number1=int(input("请输入您的身高:"))
number2=int(input("请输入您的身高:"))
number3=int(input("请输入您的身高:"))
number4=int(input("请输入您的身高:"))
max_value=number1
if max_value<number2:
    max_value=number2
if max_value<number3:
    max_value=number3
if max_value<number4:
    max_value=number4
print(max_value)