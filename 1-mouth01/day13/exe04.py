# """
#     2048 游戏核心算法
# """
list_merge = [2, 0, 2, 0]

map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [4, 4, 4, 2],
]


def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


def merge():
    """
        合并数据
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


def move_left():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge

    for line in map:
        list_merge = line
        merge()  # 操作list_merge,但是等同于操作map


# move_left()
# print(map)


# # 4. 向右移动 move_right
# def move_right():
#     """
#         向左移动map
#         思想：获取每行，交给list_merge，在通知merge()进行合并
#     :return:
#     """
#     global list_merge
#     for line in map:
#         # 从右向左获取数据形成新列表
#         list_merge = line[::-1]
#         merge()
#         line[::-1] = list_merge
#
#
# move_right()
# print(map)


def move_up():

        for r in range(3, len(map)):
            map[2][r], map[r][2] = map[r][2], map[2][r]
        for r1 in range(2, len(map)):
            map[1][r1], map[r1][1] = map[r1][1], map[1][r1]
        for r2 in range(1, len(map)):
            map[0][r2], map[r2][0] = map[r2][0], map[0][r2]


move_up()
print(map)
