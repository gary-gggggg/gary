"""打印香港疫情信息(xx 地区新增 xx 人现存 xx 人)
将地区列表后 2 个元素修改为 ["XJ","SC"]
打印地区列表元素(一行一个)
倒序打印新增列表元素(一行一个)
"""
list_region=["香港","上海","新疆"]
list_newly_comfirmed=[15,6,0]
list_comfirmed=[393,61,49]
list_region.append("四川")
list_newly_comfirmed.append(0)
list_comfirmed.append(0)
list_region.insert(0,"台湾")
list_newly_comfirmed.insert(0,0)
list_comfirmed.insert(0,19)
list_region[-2:]=["XJ","SC"]
print(f"{list_region[1]}地区新增{list_comfirmed[1]}人，\
现存{list_comfirmed[1]}")