"""确诊人数
"""
number_of_infective=int(input("enter the number of infective:"))
number_of_cured=int(input("enter the number of cured:"))
percentage_of_cured=number_of_cured/number_of_infective*100
print(str(percentage_of_cured)+"%")
