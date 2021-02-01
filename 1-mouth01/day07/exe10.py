"""3. 打印所有订单中的商品信息, 格式：商品名称 xx,商品单价:xx,数量 xx
4.0查找数量最多的订单(使用自定义算法,不使用内置函数)
5. 根据购买数量对订单列表降序(大->小)排列"""
dict_commodity_infos = {1001: {"name": "屠龙刀",\
 "price": 10000}, 1002: {"name": "倚天剑", "price": 10000}, \
 1003: {"name": "金箍棒", "price": 52100}, \
 1004: {"name": "口罩", "price": 20}, \
 1005: {"name": "酒精", "price": 30}, }# \
 # 订单列表
list_orders = [{"cid": 1001, "count": 1}, \
 {"cid": 1002, "count": 3}, {"cid": 1005, "count": 2},]
max=list_orders[0]
for i in range(1,len(list_orders)):
    if max["count"]<list_orders[i]["count"]:
        max=list_orders[i]
print(max)









