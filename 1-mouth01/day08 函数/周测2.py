"""删除列表中所有重复的元素（重复元素只保留一个）
输入：[4,35,7,64,7,35]
输出：[4,35,7,64]"""
listA=[4,35,7,64,7,35]
outcome=[]
for c in listA:
    if c not in outcome:
        outcome.append(c)
print(outcome)