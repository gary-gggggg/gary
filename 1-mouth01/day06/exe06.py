"""练习 1：
将两个列表，合并为一个字典
姓名列表["张无忌","赵敏","周芷若"]
姓名列表["张无忌","赵敏","周芷若"]
{101: '张无忌', 102: '赵敏', 103: '周芷若'}"""
list_name = ["张无忌", "赵敏", "周芷若"]
list_room = [101, 102, 103]
dict_info = {}
for i in range(len(list_name)):
    key = list_room[i]
    value = list_name[i]
    dict_info[key] = value
print(dict_info)
# dict_info = {list_room[i]: list_name[i] for i in range(len(list_name))}
# print(dict_info)
#
# dict_new = {v: k for k, v in dict_info.items()}
# print(dict_new)