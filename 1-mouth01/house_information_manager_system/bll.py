"""
    业务逻辑层
"""
from dal import HouseDao
from gongju.gongjuren import Iterablehelper


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()
        self.gonju = Iterablehelper()

    @property
    def list_houses(self):
        return self.__list_houses

    def find_the_max_price(self):
        tt1 = max(self.__list_houses, key=lambda t1: t1.total_price)
        return tt1

    def find_smallest_area(self):
        tt2 = min(self.__list_houses, key=lambda t2: t2.area)
        return tt2

    def up_order_list(self):
        tt4 = self.__list_houses[:]
        self.gonju.order_by(tt4, lambda t3: t3.total_price)
        return tt4

    def downsiding_order(self):
        tt5 = self.__list_houses[:]
        self.gonju.order_by(tt5, lambda t4: t4.area)
        return tt5

    def check_the_info_in_the_dict(self):
        final_list={}
        for t6 in self.__list_houses:
            if t6.house_type in final_list:
                final_list[t6.house_type]+=1
            else:
                final_list[t6.house_type]=1
        return final_list


