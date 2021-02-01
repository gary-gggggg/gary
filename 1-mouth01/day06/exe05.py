"""删除香港现有人数信息
删除新疆新增人数信息
删除上海的新增和现有"""
hkinfo={"region":"hk","new":15,"now have":39,"total":4801,\
            "cured":4320,"死亡":88}
shinfo={"region":"hk","new":6,"now have":61,"total":903,\
            "cured":835,"死亡":7}
xjinfo={"region":"hk","new":0,"now have":49,"total":902,\
            "cured":850,"死亡":3}
del hkinfo["now have"]
del xjinfo["new"]
del shinfo["now have"],shinfo["new"]
print(hkinfo)
print(shinfo)
print(xjinfo)
