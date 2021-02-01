"""创建电脑类,保护数据在有效范围内
        数据:型号,   CPU型号,    内存大小,    硬盘大小
                不超过10个字符    大于0    元组长度大于1
"""


class Computer:
    def __init__(self, model_number="", cpu="", memory=0, hard_disk=()):
        self.model_number = model_number
        self.cpu = cpu
        self.memory = memory
        self.hard_disk = hard_disk

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        if len(value) > 10:
            raise Exception("cpu型号太大")
        else:
            self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        if value < 0:
            raise Exception("内存太小")
        else:
            self.__memory = value

    @property
    def hard_disk(self):
        return self.__hard_disk

    @hard_disk.setter
    def hard_disk(self, value):
        if len(value) == 2:
            self.__hard_disk = value
        else:
            raise Exception("你应该有两个硬盘")


alienware = Computer("外星人ALW17M", "Intel i7", 16, (256, 1024))
print(alienware.model_number)
print(alienware.cpu)
print(alienware.memory)
print(alienware.hard_disk)
print(Computer.__dict__)