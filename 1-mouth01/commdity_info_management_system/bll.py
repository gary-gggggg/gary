from bll import *
from real.model import CommodityModel


class CommodityController:
    def __init__(self):
        self.__list_of_commodity = []
        self.number_of_cm = 1000

    @property
    def list_of_commodity(self):
        return self.__list_of_commodity

    def addto_datebase_of_Commodityinfo(self, comdity_info):
        comdity_info.cm = self.number_of_cm
        self.number_of_cm += 1
        self.__list_of_commodity.append(comdity_info)

    def removed_info(self, cm):
        cm1 = CommodityModel(cm=cm)
        if cm1 in self.__list_of_commodity:
            self.__list_of_commodity.remove(cm1)
            return True
        else:
            return False

    def update_info(self, ccm):
        for i in self.__list_of_commodity:
            if i.cm == ccm.cm:
                i.__dict__ = ccm.__dict__
                return True
            return False
