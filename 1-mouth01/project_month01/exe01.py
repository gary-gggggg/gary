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
        for i in self.__controller.list_of_commodity:
            print(i)

    def __remove_commodity_info(self):
        cm = int(input("请输入您要删除的商品的商品识别码："))
        if self.__controller.removed_info(cm):
            print("删除成功")
        else:
            print("删除失败")

    def __update_commodity_info(self):
        ccm = CommodityModel()
        ccm.cm = int(input("请输入您需要修改的商品的编号："))
        ccm.cid = input("请输入商品编号")
        ccm.name = input("请输入商名称")
        ccm.price = input("请输入商品价格")
        if self.__controller.update_info(ccm):
            print("修改成功")
        else:
            print("修改失败")


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


v = CommodityView()
v.main()
