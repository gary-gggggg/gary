"""练习：在终端中,循环录入字符串,
如果录入空则停止.
停止录入后打印所有内容(一个字符)
效果：
请输入内容：香港
请输入内容：上海
请输入内容：新疆
请输入内容：
香港_上海_新疆"""
sum=[]
while True:
    region=input("请输入内容：")
    if region=="":
        break
    sum.append(str(region))
    result="_".join(list_region)
print(sum)

