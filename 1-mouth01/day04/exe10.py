"""提取变量后，用字符串格式话的方式打印信息"""
confirmed=int(input("请输入确证人数："))
cured=int(input("请输入治愈人数："))
cured_rate=float(input("请输入治愈率："))
print("湖北确诊人数%.2d人,治愈%.2d人,治愈率%.2f" %(confirmed, cured, cured_rate))