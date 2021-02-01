"""画出内存图，出结果
"""
name_of_beijing,region = "北京","市"
name_of_beijing_region=name_of_beijing+region
region="省"
print(name_of_beijing_region)
del name_of_beijing
print(name_of_beijing_region)