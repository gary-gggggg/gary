"""练习 3：多个人的多个爱好
dict_hobbies = { "于谦": ["抽烟", "喝酒", "烫头"], "郭德纲": ["说", "学", "逗", "唱"],
}
1. 打印于谦的所有爱好(一行一个)
效果：抽烟
喝酒
烫头
2. 计算郭德纲所有爱好数量
效果：4
3. 打印所有人(一行一个)
效果：于谦
郭德纲
4. 打印所有爱好(一行一个)
抽烟
喝酒
烫头
说
学
逗
唱"""
dict_hobbies = {"于谦": ["抽烟", "喝酒", "烫头"],\
                "郭德纲": ["说", "学", "逗", "唱"],
                }
for l in dict_hobbies["于谦"]:
    print(l)
print(len(dict_hobbies["郭德纲"]))
for k in dict_hobbies.keys():
    print(k)
for v in dict_hobbies.values():
    for l2 in v:
        print(l2)

