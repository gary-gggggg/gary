# """
# 4. 小明使用手机打电话
#    要求:增加座机,卫星电话时不影响小明.
# """
#
#
# class Person:
#     def __init__(self, name="", communnicate=None):
#         self.name = name
#         self.communnicate = communnicate
#
#     def calling(self, tool):
#         print("打电话")
#         tool.damage(self.communnicate)
#
#
# class CommunnicateTool:
#     def damage(self, value):
#         print("giao")
#
#
# class Phone(CommunnicateTool):
#     def damage(self, value):
#         print("使用手机")
#
#
# class SetteledPhone(CommunnicateTool):
#     def damage(self, value):
#         print("使用座机")
#
#
# class StelaiesPhone(CommunnicateTool):
#     def damage(self, value):
#         print("使用卫星电话")
#
#
# xm = Person("小明")
# xm.calling(Phone())
# xm.calling(SetteledPhone())
# xm.calling(StelaiesPhone())
# xm.calling(CommunnicateTool())
class haha:
    def mydo(self,v):
        print('giao',v)

class aha(haha):
    def hedo(self):
        haha.mydo(self,'j')
        print('cao')
res = aha()
res.hedo()