"""终端中输入字，ord成逐个的翻译成数字"""
unit=input("请输入您的想要翻译的内容：")
for i in unit:
    result=ord(i)
    print(result)
