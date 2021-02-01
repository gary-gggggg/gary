"""练习：累加 10 -- 60 之间个位不是 3/5/8 的整数和"""
sum=0
for i in range(10,61):
    if i%10==3 or i%10==5 or i %10==8:
        continue
    sum+=i
print(sum)
