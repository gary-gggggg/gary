"""3. 将列表中的数字累减
    list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    提示：初始为第一个元素"""
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
start=list02[0]
for i in list02[1:len(list02)]:
    start-=int(i)
print(start)

