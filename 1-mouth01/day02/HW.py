"""根据父母身高,预测儿子身高.
    步骤:获取父亲身高
        获取母亲身高
        显示儿子身高
    公式:(父亲身高+母亲身高)*0.54"""
hight_father=float(input("请输入父亲身高："))
hight_mother=float(input("请输入母亲身高："))
print("儿子的身高是"+str((hight_father+hight_mother)*0.54))

