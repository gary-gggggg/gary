"""创建函数,根据年龄计算人生阶段
age = int(input("请输入年龄："))
if age <= 6: print("童年")
elif age <= 17: # 程序能执行到本行,说明 age 一定大于 6
print("少年")
elif age <= 40: print("青年")
elif age <= 65: print("中年")
else: print("老年")"""


def identify_age(age):
    if age <= 6: return "童年"
    if age <= 17: return "少年"
    if age <= 40: return "青年"
    if age <= 65: return "中年"
    return "老年"

zage=int(input("请输入年龄："))
result=identify_age(zage)
print(result)