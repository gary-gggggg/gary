from bll import HouseManagerController


class HouseView:
    def __init__(self):
        self.__housem = HouseManagerController()

    def __menu_show(self):
        print("按1显示房源")
        print("2键显示总价最高的房源信息")
        print("3键显示面积最小的房源信息")
        print("4键根据总价升序显示房源信息")
        print("按5键根据面积降序显示房源信息")
        print("6键查看房源类型信息")
        self.__menu_select()

    def __menu_select(self):
        menu_number = int(input("请输入您的数字："))
        if menu_number == 1:
            self.__show_houses()
        if menu_number==2:
            self.__find_the_max_price()
        if menu_number==3:
            self.__find_smallest_area()
        if menu_number==4:
            self.__up_order_list()
        if menu_number==5:
            self.__downsing_order()
        if menu_number==6:
            self.__check_the_info_in_the_dict()
    def __show_houses(self):
        for house in self.__housem.list_houses:
            # 直接打印对象,由对象的__str__方法决定打印风格
            print(house.__dict__)

    def main(self):
        while 1:
            self.__menu_show()
            self.__menu_select()

    def __find_the_max_price(self):
        print(self.__housem.find_the_max_price().__dict__)

    def __find_smallest_area(self):
        print(self.__housem.find_smallest_area().__dict__)

    def __up_order_list(self):
        t4=self.__housem.up_order_list()
        for ttt4 in t4:
            print(ttt4.__dict__)


    def __downsing_order(self):
        t5=self.__housem.downsiding_order()
        for ttt5 in t5:
            print(ttt5.__dict__)

    def __check_the_info_in_the_dict(self):
        t6=self.__housem.check_the_info_in_the_dict()
        for k,v in t6.items():
            print(f"{k}的房子一共有{v}个")


k=HouseView()
k.main()









