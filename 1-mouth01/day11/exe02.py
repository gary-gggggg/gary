"""小明请保洁保洁打扫卫生

"""


# class Person:
#     def __init__(self, name=""):
#         self.name=name
#
#     def inviting(self):
#         print("请")
#         job=Worker()
#         job.clenning()
#
# class Person:
#     def __init__(self, name=""):
#         self.name=name
#         self.__worker=Worker()
#
#     def inviting(self):
#         print("请")
#         self.__worker.clenning()




class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self,cleaner):
        print("通知")
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Client("小明")
cleaner = Cleaner()
xm.notify(cleaner)
print(isinstance(xm, Cleaner))