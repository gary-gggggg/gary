"""在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"""
zdic={"R":"红色",\
      "G":"绿色",\
      "B":"蓝色",\
      "A":"透明度"}
while 1:
    x=input("请输入相应的颜色(R/G/B/A)：")
    if x not in zdic:
        print("颜色不存在")
        pass
    else:
        print(zdic[x])
        break
