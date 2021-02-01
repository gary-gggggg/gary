"""
练习2： 拷贝一个目录
假设目录下有若干普通文件,需要编写程序
将该目录拷贝一份，注意拷贝过程中需要
多文件同时拷贝（使用进程池完成）
os.mkdir("FTP")
os.listdir("/home/tarena/FTP")
"""
from multiprocessing import Pool, Queue
import os

qq = Queue()  # 生成消息队列


# 进程池事件 将文件从原文件夹拷贝到新文件夹
def copy(filename, old, new):
    fr = open(old + '/' + filename, 'rb')
    fw = open(new + '/' + filename, 'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
        n = fw.write(data)
        qq.put(n)
    fr.close()
    fw.close()


def get_size(dir):
    res = 0
    for f in os.listdir(dir):
        res += os.path.getsize(f)
    return res


# 创建进程池，调用函数作为进程池执行事件
def main(old_folder):
    # 创建新文件夹
    new_folder = old_folder.split("/")[-1]
    os.mkdir(new_folder)

    # 获取文件里列表
    file_list = os.listdir(old_folder)

    tt_size = get_size(old_folder)
    # 创建进程池
    pool = Pool()
    # 循环添加事件
    for file in file_list:
        pool.apply_async(copy, args=(file, old_folder, new_folder))
    pool.close()
    copy_size = 0
    while copy_size < tt_size:
        copy_size += qq.get()
        print("已拷贝%.2f%%" % (copy_size / tt_size * 100))
    pool.join()


if __name__ == '__main__':
    main("/home/tarena/FTP")
