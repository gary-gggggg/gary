""" 如果是vip客户,消费小于等于500,享受85折
                    消费大于500,享受8折
        如果不是vip客户,消费大于等于800,享受9折
                      消费小于800,原价
        在终端中输入账户类型,消费金额,计算折扣."""
type_of_customer=input("您是否是vip：")
money=int(input("您的消费金额是多少？"))
if type_of_customer=="是":
    discount=85 if money<=500 else 8
else:
    discount=9 if money>=800 else "原价"
print(str(discount)+"折")