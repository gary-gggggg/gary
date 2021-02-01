import copy
list01 = ["北京",["上海","深圳"]]
list02 = list01
list03 = list01[:]
list04 = copy.deepcopy(list01)
list04[0] = "北京 04"
list04[1][1] = "深圳 04"
print(list01)
list03[0] = "北京 03"
list03[1][1] = "深圳 03"
print(list01)
list02[0] = "北京 02"
list02[1][1] = "深圳 02"
print(list02)
