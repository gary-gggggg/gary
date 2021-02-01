"""判断二维数字列表中是否存在某个数字
输入：二维列表,11
输出:True"""

def indentify(l1):
    for c in l1:
        if 11 in c:
            return True



list1 = [[15], [15, 689], [11, 456], [78, 3694, 45], [17, 158], \
         [9], [75], [164, 11]]
result=indentify(list1)
print(result)