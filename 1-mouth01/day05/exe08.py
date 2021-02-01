"""练习：生成 10--30 之间
能被 3 或者 5 整除的数字[10, 12, 15, 18, 20, 21, 24, 25, 27]
生成 5 -- 20 之间的
数字平方[25, 36, 49, 64, 81, 100, 121, 144,
169, 196, 225, 256, 289, 324, 36"""
list_number1=[10,12,15,18,20,21,24,25,27]
# giao=[]
# for i in list_number1:
#     if i%3==0 or i%5==0:
#         giao.append(i)
# print(giao)

giaoz=[i for i in list_number1 if i%3==0 or i%5==0]
print(giaoz)

giao=[l**2 for l in range(5,21)]
print(giao)