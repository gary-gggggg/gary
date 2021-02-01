class Iterablehelper:
    @staticmethod
    def find_singel01(kdddx, l0):
        """

        :param kdddx: 输入可迭代对象
        :param l0: 目标函数
        :return: 返回单一值
        """
        for item in kdddx:
            if l0(item):
                return item


    @staticmethod
    def find_count(kdddx, l3):
        """

        :param kdddx: 输入可迭代对象
        :param l3: 目标函数
        :return: 返回目标数量
        """
        count=0
        for item in kdddx:
            if l3(item):
                count+=1
        return count

    @staticmethod
    def find_all(kdddx1, l):
        """

        :param kdddx1: 输入可迭代对象
        :param l: 目标函数
        :return: 返回一列生成器
        """
        for i in kdddx1:
            if l(i):
                yield i

    @staticmethod
    def find_min(kdddx2, l1):
        """

        :param kdddx2: 输入可迭代对象
        :param l1: 目标函数
        :return: 返回最小值
        """
        mins = l1(kdddx2[0])
        for c in range(1, len(kdddx2)):
            if l1(kdddx2[c]) < mins:
                mins = l1(kdddx2[c])
        return mins

    @staticmethod
    def order_by(kdddx3, l2):
        """

        :param kdddx3: 输入可迭代对象
        :param l2: 目标函数
        :return: 根据函数属性对可迭代进行升序处理
        """
        for i1 in range(len(kdddx3) - 1):
            for i2 in range(i1 + 1, len(kdddx3)):
                if l2(kdddx3[i2]) < l2(kdddx3[i1]):
                    kdddx3[i2], kdddx3[i1] = kdddx3[i1], kdddx3[i2]
        return kdddx3
