"""根据工资计算个人社保缴纳费用
    步骤：在终端中录入工资,根据公式计算,显示缴纳费用
    公式：养老保险8% + 医疗保险2% + 3元 + 失业保险0.2% + 公积金12%"""
salary=float(input("请输入您的工资："))
result=salary*0.08
result+=salary*0.02
result+=3
result+=salary*0.002
result+=salary*0.12
print(result)
