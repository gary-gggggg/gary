"""选做)一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)
    -- 全过程总共移动多少米?
   提示:
       数据/算法"""
times=0
r=0
hight=float(input("请输入下落的高度："))
while True:
    sum=hight+hight/2
    r+=sum
    hight=hight/2
    if hight<=0.01:
        break
    times+=1
print("一共弹了%d次，共移动%.9f米"%(times,r))

