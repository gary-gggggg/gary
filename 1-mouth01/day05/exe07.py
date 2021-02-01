"""2. 列表转换为字符串：列表 = “a-b-c-d”.split(“分隔符”)练习：
将下列英文语句按照单词进行翻转. 转换前：To have a government that is
of people by people for people
转换后：people for people by people of is that government a have To
"""
list_yuan="To have a government that is \
of people by people for people"
dates=list_yuan.split(" ")
giao=" ".join(dates[::-1])
print(giao)