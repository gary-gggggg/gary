"""练习 1：对象计数器统计构造函数执行的次数
使用类变量实现
画出内存图
class Wife:
pass
w01 = Wife("双儿")
w02 = Wife("阿珂")
w03 = Wife("苏荃")
w04 = Wife("丽丽")
w05 = Wife("芳芳")
print(w05.count) # 5
Wife.print_count()# 总共娶了 5 个"""


class Wife:
    total_number_of_wify = 0
    @classmethod
    def func(cls):
        print(f"总共娶了{cls.total_number_of_wify}个")

    def __init__(self, wife, ):
        self.wife = wife
        Wife.total_number_of_wify += 1




w01 = Wife("双儿")
w02 = Wife("阿珂")
w03 = Wife("苏荃")
w04 = Wife("丽丽")
w05 = Wife("芳芳")
print(w05.total_number_of_wify)
Wife.func()
