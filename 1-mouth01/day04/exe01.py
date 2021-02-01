"""在终端中输入任意整数，计算累加和.
"1234" -> "1" -> 累加 1
效果：
请输入一个整数:12345
累加和是 15"""
number=input("请输入您的数字：")
sum=0
for i in number:
    sum+=int(i)
print(sum)

