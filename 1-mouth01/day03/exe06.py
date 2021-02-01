"""根据心理年龄与实际年龄，打印智商等级。
智商 IQ = 心理年龄 MA 除以 实际年龄 CA 乘以 100
天才：140 以上（包含）
超常：120-139 之间（包含）
聪慧：110-119 之间（包含）
正常：90-109 之间（包含）
迟钝：80-89 之间（包含）
低能：80 以下"""
mind_age=int(input("输入心里年龄:"))
actrual_age=int(input("输入实际年龄:"))
IQ=mind_age/actrual_age*100
if IQ>=140:
    print("天才")
elif 120<=IQ:
    print("超常")
elif 110<=IQ:
    print("聪慧")
elif 90<=IQ:
    print("正常")
elif 80<=IQ:
    print("迟钝")
else:
    print("低能")