"""在终端中打印香港字典的所有键(一行一个)
在终端中打印上海字典的所有值(一行一个)
在终端中打印新疆字典的所有键和值(一行一个)
在上海字典中查找值是 61 对应的键名称"""
hkinfo={"region":"hk","new":15,"now have":39,"total":4801,\
            "cured":4320,"死亡":88}
shinfo={"region":"hk","new":6,"now have":61,"total":903,\
            "cured":835,"死亡":7}
xjinfo={"region":"hk","new":0,"now have":49,"total":902,\
            "cured":850,"死亡":3}
for k in hkinfo:
    print(k)
for v in shinfo.values():
    print(v)
for i in xjinfo.items():
    print(i)
for k2,v2 in shinfo.items():
    if v2==61:
        print(k2)
        break

