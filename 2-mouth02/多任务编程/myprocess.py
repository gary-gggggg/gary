from multiprocessing import Process


def gggg():
    print("成功")


# 使用面向对象 创建自己的进程类
class MyProcess(Process):
    def __init__(self):
        super().__init__(target=gggg)


    # # 进程的入口函数
    # def run(self):
    #     print("我TM干爆")


gg = MyProcess()
# 使用父类功能并且启动进程
gg.start()  # start()调用解释器去调用run()
gg.join()
