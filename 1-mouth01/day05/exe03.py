"""练习 4：在地区列表中删除“新疆”
在新增列表中删除第 1 个元素
在现有列表中删除前 2 个"""
list_region=["香港","上海","新疆"]
list_newly_comfirmed=[15,6,0]
list_comfirmed=[393,61,49,1465,458,48]
if "新疆" in list_region:
    list_region.remove("新疆")
del list_newly_comfirmed[0]
del list_comfirmed[:2]
print(list_region,\
      list_newly_comfirmed,\
      list_comfirmed)