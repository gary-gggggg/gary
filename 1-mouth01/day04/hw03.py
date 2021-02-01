""" (选做)赌大小游戏
    玩家的身家初始10000，实现下列效果：
        少侠请下注: 30000
        超出了你的身家，请重新投注。
        少侠请下注: 8000
        你摇出了5点,庄家摇出了3点
        恭喜啦，你赢了，继续赌下去早晚会输光的，身家还剩18000
        少侠请下注: 18000
        你摇出了6点,庄家摇出了6点
        打平了，少侠，在来一局？
        少侠请下注: 18000
        你摇出了4点,庄家摇出了6点
        少侠,你输了，身家还剩 0
        哈哈哈，少侠你已经破产，无资格进行游戏"""
m=10000
while m>0:
    bet=float(input("少侠请下注："))
    if bet>m:
        print("穷光蛋，滚！")
        continue
    import random
    ur_number=random.randint (1,6)
    host_number=random.randint (1,6)
    print("你摇出了%d,庄摇出了%d"%(ur_number,host_number))
    if ur_number>host_number:
        m+=bet
        print("你可真他妈牛逼，身价已经有%.1f了"%(m))
    elif ur_number==host_number:
        print("运气不错啊，竟然平局让你逃过一劫。")
    else:
        m-=bet
        if m==0:
            print("滚吧，你已经没钱了")
        else:
            print("垃圾，身价已经变成%.1f了，迟早没钱"%(m))

