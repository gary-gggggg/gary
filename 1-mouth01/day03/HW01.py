"""(1) 电梯设置规定：
            如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，
            否则提示超载。
        步骤:
            终端中获取人数/总重量
            显示电梯正常运行
                电梯超载"""
person, weight=int(input("请输入人数：")),int(input("请输入总重量(kg)："))
result="电梯正常运行" if person<= 10 and weight<=1000 else "电梯超载"
print(result)




