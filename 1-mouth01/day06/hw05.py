"""将列表中所有元素转换为一个字符串
    列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
    结果:我爱你python666"""
row_list=["我", "爱", "你", "p", "y", "t", "h", "o", "n", ]
new_list="".join(row_list[:-1])
print(f"{new_list}{row_list[-1]}")
