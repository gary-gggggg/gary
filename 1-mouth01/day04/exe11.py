"""字符串格式化练习"""
second=float(input("请输入秒数："))
minit= second//60
rsecond=second%60
print("%.2f秒是%.2d分钟%.f秒" %(second,minit,rsecond))
