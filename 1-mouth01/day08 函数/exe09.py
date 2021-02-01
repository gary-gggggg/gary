"""根据下列代码，创建降序排列函数。
list01 = [5, 15, 25, 35, 1, 2]
for r in range(len(list01) - 1): for c in range(r + 1, len(list01)): if list01[r] < list01[c]: list01[r], list01[c] = list01[c], list01[r]
print(list01)"""


def decline_order(fuck):
    for r in range(len(fuck) - 1):
        for c in range(r + 1, len(fuck)):
            if fuck[r] < fuck[c]:
                fuck[r], fuck[c] = fuck[c], fuck[r]


list01 = [5, 15, 25, 35, 1, 2]
decline_order(list01)
print(list01)
