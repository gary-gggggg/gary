"""外挂1"""

wg1 = 5
wg2 = 0
while True:
    n1 = input("输入您的红包数量：")
    if n1 == " " or n1 == "exit":
        break
    n2=float(n1)
    if n2>= 5:
        wg2 += 1
    if n2 >= 10:
        wg1 += 1
print(wg1, wg2)



