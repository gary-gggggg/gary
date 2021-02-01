class Model:
    def __init__(self, word=""):
        self.word = word


class View:
    def __init__(self, controler=""):
        self.__controler = Controller()

    def __show_menu(self):
        print("输入单词获得相应解释")
        self.__select_menu()

    def __select_menu(self):
        word = input("请输入数字：")
        self.__show_ex(word)

    def main(self):
        while 1:
            self.__show_menu()
            self.__select_menu()

    def __show_ex(self, n):
        self.__controler.show_the_expanlination(n)


class Controller:
    total_dict = open("dict.txt", "r")

    def show_the_expanlination(self, word):
        for k in Controller.total_dict:
            tmp = k.split(" ", 1)
            if tmp[0] > word:
                return ("输入错误")
            elif word == tmp[0]:
                print(tmp[1].strip())


tt = View()
tt.main()
