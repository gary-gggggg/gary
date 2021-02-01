"""八大行星："水星" "金星" "地球" "火星" "木星" "土星" "天王星" "海王星" --
 创建列表存储 4 个行星：“水星” "金星" "火星" "木星" --
 插入"地球"、追加"土星" "天王星" "海王星" --
 打印距离太阳最近、最远的行星(第一个和最后一个元素) --
 打印太阳到地球之间的行星(前两个行星) --
 删除"海王星",删除第四个行星
-- 倒序打印所有行星(一行一个)"""
lise_planet=["水星", "金星", "火星", "木星"]
lise_planet.insert(2,"地球")
lise_planet.append("土星")
lise_planet.append("天王星")
lise_planet.append("海王星")
print(lise_planet[0],lise_planet[-1])
print(lise_planet[:3])
lise_planet.remove("海王星")
del lise_planet[3]
for i in range(len(lise_planet)(-1:-1:1)):
    print(i)