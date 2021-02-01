"""1. 在商品列表，获取所有名称与单价
2. 在商品列表中，获取所有单价小于 10000 的商品
3. 对商品列表，根据单价进行降序排列
4. ([1,1],[2,2,2],[3,3,3])"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [Commodity(1001, "屠龙刀", 10000),
                        Commodity(1002, "倚天剑", 10000),
                        Commodity(1003, "金箍棒", 52100),
                        Commodity(1004, "口罩", 20),
                        Commodity(1005, "酒精", 30)]

tuple01 = ([1, 1], [2, 2, 2], [3, 3, 3])

for t1 in map(lambda g: g, list_commodity_infos):
    print(t1.__dict__)
for t2 in filter(lambda g2: g2.price < 10000, list_commodity_infos):
    print(t2.__dict__)
new_list = sorted(list_commodity_infos, key=lambda g3: g3.price, reverse=1)
for t3 in new_list:
    print(t3.__dict__)

for t4 in filter(lambda g4: len(g4) == len(max(tuple01, key=len)), tuple01):
    print(t4)


