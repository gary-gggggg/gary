# --------------------------数据--------------------------
# 商品列表
# 字典更擅长定位单个元素
# dict_commodity_infos = {
#     1001:{"name": "屠龙刀", "price": 10000},
#     1002:{"name": "倚天剑", "price": 10000},
#     1003:{"name": "金箍棒", "price": 52100},
#     1004:{"name": "口罩", "price": 20},
#     1005:{"name": "酒精", "price": 30},
# }
# 列表更擅长按某种顺序定位元素
#
class ListOrders:
    def __init__(self, cid, count):
        self.cid = cid
        self.count = count


class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


# -------------全局变量----------------
list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30), ]

# 订单列表
list_orders = [
    ListOrders(1001, 1),
    ListOrders(1002, 3),
    ListOrders(1005, 2),
]


# -------------函数----------------

def print_single_commodity(commodity):
    print(f"编号:{commodity.cid},商品名称:{commodity.name},商品单价:{commodity.name}")


# 1.  定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_infos():
    for commodity in list_commodity_infos:
        # print(f"编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")
        print_single_commodity(commodity)


# 2.  定义函数,打印商品单价小于2万的商品信息
def print_price_in_2w():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            # print(f"编号:{commodity['cid']}商品名称:{commodity['name']}商品单价:{commodity['price']}")
            print_single_commodity(commodity)


# 3.  定义函数,打印所有订单中的商品信息,
#   格式：商品名称xx,商品单价:xx,数量xx.
def print_order_infos():
    for order in list_orders:  # 遍历所有订单
        # order["cid"] --> 1001  -->
        for commodity in list_commodity_infos:  # 遍历所有商品信息
            # commodity["cid"] --> 1001
            # 使用订单中的商品编号 在 商品信息中查找(商品)
            if list_orders == commodity.cid:
                print(f"商品名称{commodity.name},商品单价:{commodity['price']},数量{order['count']}.")
                break  # 跳出内层循环


# 4. 定义函数,在商品列表中查找最贵的商品
def get_max_commodity_by_price():
    min_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if min_value.price > list_commodity_infos[i].price:
            min_value = list_commodity_infos[i]
    return min_value


# 5. 定义函数,根据单价对商品列表升序排列
def ascending_commodity_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price > list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


# 6. 定义函数,删除单价大于5000的商品
def delete_commodity_gt_5000_by_price():
    for i in range(len(list_commodity_infos) - 1, -1, -1):
        if list_commodity_infos[i].price > 5000:
            del list_commodity_infos[i]


# -------------入口--------------
print_commodity_infos()
print_price_in_2w()
print_order_infos()
cc=get_max_commodity_by_price()
print_single_commodity(cc)

