"""如果账号的密码错误3次，提示锁定账户，效果如下：
        请输入账号：qtx
        请输入密码：1234
        登录失败
        你还剩余 2 次机会
        请输入账号：Qtx
        请输入密码：1234
        登录失败
        你还剩余 1 次机会
        请输入账号：Qtx
        请输入密码：123456
        登录成功"""
t=0
while t<=3:
    t+=1
    if input("请输入账号：")!="Qtx"or input\
                ("请输入密码：")!="123456":
        print("登录失败！"
              "你还有%d次机会"%(3-t))
    else:
        print("登录成功，你个小滑头！")

