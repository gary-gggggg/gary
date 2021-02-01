"""
    数据访问层
    data access layer
"""
import csv
from typing import List

from model import HouseModel

class HouseDao:
    """
        房源数据访问对象
    """
    __house_data = []  # type:List[HouseModel]
    __FILE_NAME = "/home/tarena/PycharmProjects/untitled/house_information_manager_system/house.csv"

    @classmethod
    def load(cls) -> List[HouseModel]:
        """
            加载房源信息
        :return:文件中所有房源信息
        """
        cls.__house_data.clear()
        # 打开文件
        with open(cls.__FILE_NAME,encoding="utf-8") as csvfile:
            # 使用csv模块读取数据
            for row in csv.reader(csvfile):
                model = cls.__string_to_HouseModel(row)
                cls.__house_data.append(model)
        return cls.__house_data

    @staticmethod
    def __string_to_HouseModel(line):
        return HouseModel(int(line[0]), line[1], line[2], line[3], line[4], float(line[5]), line[6], line[7],
                          float(line[8]), float(line[9]), line[10])

    @classmethod
    def save(cls) -> None:
        """
            保存房源信息
        """
        with open(cls.__FILE_NAME, "w") as csvfile:
            csv_writer = csv.writer(csvfile)
            for house in cls.__house_data:
                csv_writer.writerow(house.__dict__.values())


if __name__ == '__main__':
    # 测试代码
    for item in HouseDao.load():
        print(item.__dict__)