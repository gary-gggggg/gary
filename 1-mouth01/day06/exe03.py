"""在终端中打印香港的现有人数
在终端中打印上海的新增和现有人数
新疆新增人数增加 1
"""
hkinfo={"region":"hk","new":15,"now have":39,"total":4801,\
            "cured":4320,"死亡":88}
shinfo={"region":"hk","new":6,"now have":61,"total":903,\
            "cured":835,"死亡":7}
xjinfo={"region":"hk","new":0,"now have":49,"total":902,\
            "cured":850,"死亡":3}
print(hkinfo["now have"])
print(shinfo["new"])
print(shinfo["now have"])
xjinfo["new"]=1
print(xjinfo)