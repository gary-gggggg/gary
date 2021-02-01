"""6. 作用：实现 python 装饰器练习：
使用闭包模拟以下情景：在银行开户存入 10000
购买 xx 商品花了 xx 元
购买 xx 商品花了 xx元"""


def deposit(money):
    print(f"存了{money}")
    def spend_money(commdity, price):
        nonlocal money
        money -= price
        print(f"购买{commdity}商品花了{price}元，还剩{money}元")
    return spend_money


result = deposit(10000)
result("充气娃娃",9999)

