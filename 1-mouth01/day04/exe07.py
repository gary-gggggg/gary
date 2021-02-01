"""1-100随机数字，猜数字游戏
程序产生 1 个,1 到 100 之间的随机数。
让玩家重复猜测,直到猜对为止。
每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
效果：
请输入要猜的数字:50
大了
请输入要猜的数字:25
小了
请输入要猜的数字:35
大了
请输入要猜的数字:30
小了
请输入要猜的数字:32
恭喜猜对啦,总共猜了 5 次"""
sum=0
import random
number= random.randint (1,100)
while sum<8:
    n1=int(input("请输入数字："))
    sum += 1
    if number<n1:
        print("大了")
    elif number>n1:
        print("小了")
    else:
        print("你真牛逼!花了"+str(sum)+"次就猜对了！")
        break
else:
    print("游戏失败")


