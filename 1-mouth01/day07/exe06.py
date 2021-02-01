"""练习 4：
dict_travel_info = { "北京": { "景区": ["长城", "故宫"], "美食": ["烤鸭", "豆汁焦圈", "炸酱面"]
},"四川": { "景区": ["九寨沟", "峨眉山"], "美食": ["火锅", "兔头"]
}
}
1. 打印北京的第一个景区
效果：长城
打印四川的第二个美食
效果：兔头
2. 所有城市 (一行一个)
效果：北京
四川
3. 北京所有美食(一行一个)
效果：烤鸭
豆汁焦圈
炸酱面
4. 打印所有城市的所有美食(一行一个)
效果：烤鸭
豆汁焦圈
炸酱面
火锅
兔头"""
dict_travel_info = { "北京": { "景区": ["长城", "故宫"], \
                             "美食": ["烤鸭", "豆汁焦圈", "炸酱面"]
},"四川": { "景区": ["九寨沟", "峨眉山"], \
          "美食": ["火锅", "兔头"]}}
print(dict_travel_info["北京"]["景区"][0])
print(dict_travel_info["四川"]["美食"][1])
for l2 in dict_travel_info:
    print(l2)
for l in range(len(dict_travel_info["北京"]["美食"])):
    print(dict_travel_info["北京"]["美食"][l])
for v in dict_travel_info.values():
    for i in v["美食"]:
        print(i)






