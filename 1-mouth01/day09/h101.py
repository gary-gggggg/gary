"""
(1) 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
(2) 定义函数,打印商品单价小于2万的商品信息
(3) 定义函数,打印所有订单中的商品信息,
    格式：商品名称xx,商品单价:xx,数量xx.
(4) 定义函数,在商品列表中查找最贵的商品
(5) 定义函数,根据单价对商品列表升序排列
(6) 定义函数,删除单价大于5000的商品"""
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]

list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


def giao1():
    for i in list_commodity_infos:
        print(f"商品编号{[i["cid"]},商品名称{i["name"]},商品单价{i["price"]}")


giao1()


def giao2():
    for c in list_commodity_infos:
        if c["price"] < 20000:
            return c["cid"], c["name"], c["price"]


def giao3():
    for i1 in list_orders:
        return i1["cid"], i1["count"]


def giao4():
    max_mo = list_commodity_infos[0]
    for l in range(len(list_commodity_infos)):
        if max_mo["price"] < list_commodity_infos[l][price]:
            max_mo = list_commodity_infos[l]
            return max_mo

# def giao5():
