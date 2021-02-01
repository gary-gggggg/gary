from bll import *
class CommodityModel:
    def __init__(self, cid=0, name="", price=0, cm=0):
        self.cid = cid
        self.name = name
        self.price = price
        self.cm = cm

    def __str__(self):
        return f"商品名称是{self.name}，编号是{self.cid}，价格是{self.price}，识别码是{self.cm}"

    def __eq__(self, other):
        return self.cm == other.cm