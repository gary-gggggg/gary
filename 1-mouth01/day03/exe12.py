"""练习 4：
一张纸的厚度是 0.01 毫米
请计算，对折多少次超过珠穆朗玛峰(8844.43 米)
思路:数据:厚度 高度 次数
算法:厚度*=2 次数+=1"""
c=0.01
c1=0
while c<8844430:
    c*=2
    c1+=1
print(str(c1))
