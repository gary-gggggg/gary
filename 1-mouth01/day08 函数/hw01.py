"""参照下列代码,定义函数,计算社保缴纳费用.
    salary_before_tax = float(input("请输入税前工资："))
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    print("个人需要缴纳社保费用：" + str(social_insurance))"""
def giao(n):
    jresult=n * (0.08 + 0.02 + 0.002 + 0.12) + 3
    return jresult


salary_before_tax = float(input("请输入税前工资："))
result=giao(salary_before_tax)
print("个人需要缴纳社保费用：" + str(result))