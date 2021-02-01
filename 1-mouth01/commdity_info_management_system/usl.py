from bll import *
from real.model import CommodityModel

from commdity_info_management_system.bll import CommodityController


class CommodityView:
    def __init__(self):
        self.__controller = CommodityController()

    def __display_veiw_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")

    def __select_menu(self):
        giao = int(input("请输入按键"))
        if giao == 1:
            self.__input_commodity_info()
        elif giao == 2:
            self.__display_commodity_info()
        elif giao == 3:
            self.__remove_commodity_info()
        elif giao == 4:
            self.__update_commodity_info()

    def __input_commodity_info(self):
        """

        :return:
        """
        ccm = CommodityModel()
        ccm.name = input("请输入商品名称:")
        ccm.price = int(input("请输入商品价格:"))
        ccm.cid = int(input("请输入商品编号:"))
        self.__controller.addto_datebase_of_Commodityinfo(ccm)
        print("成功！！！")

    def main(self):
        while 1:
            self.__display_veiw_menu()
            self.__select_menu()

    def __display_commodity_info(self):
        """

        :return:
        """
        for i in self.__controller.list_of_commodity:
            print(i)

    def __remove_commodity_info(self):
        """

        :return:
        """
        cm = int(input("请输入您要删除的商品的商品识别码："))
        if self.__controller.removed_info(cm):
            print("删除成功")
        else:
            print("删除失败")

    def __update_commodity_info(self):
        """

        :return:
        """
        ccm = CommodityModel()
        ccm.cm = int(input("请输入您需要修改的商品的编号："))
        ccm.cid = input("请输入商品编号")
        ccm.name = input("请输入商名称")
        ccm.price = input("请输入商品价格")
        if self.__controller.update_info(ccm):
            print("修改成功")
        else:
            print("修改失败")
