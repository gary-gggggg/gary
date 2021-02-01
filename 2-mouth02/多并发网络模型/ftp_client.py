"""
文件服务器 客户端
"""
from socket import *
import sys
from time import sleep


class FTPHandle:
    server_address = ('127.0.0.1', 8882)

    def __init__(self):
        self.sock = self.connect_server()

    def connect_server(self):
        sockfd = socket()
        sockfd.connect(FTPHandle.server_address)
        return sockfd

    def do_list(self):
        # 发送请求
        self.sock.send(b"LIST")
        # 等待响应
        result = self.sock.recv(128).decode()
        if result == "OK":
            # 接收文件列表
            files = self.sock.recv(1024 * 1024)
            print(files.decode())
        else:
            print("文件库为空")

    def do_quit(self):
        gg = self.connect_server()
        self.sock.close()
        sys.exit("已退出!")

    def do_upload(self, filename):
        data = "PUT " + filename
        self.sock.send(data.encode())
        result=self.sock.recv(1024)
        if result==b"OK":
            try:
                file=open(filename,"rb")
            except FileNotFoundError:
                print("没有该文件")
                return
            else:
                while 1:
                    data_f=file.read(1024)
                    if not data_f:
                        break
                    self.sock.send(data_f)
                sleep(0.1)
                self.sock.send(b"##^&*")
                file.close()
                print("上传成功！")
        else:
            print("文件已存在！")


    def do_get(self, filename):
        data = "GET " + filename
        self.sock.send(data.encode())
        result = self.sock.recv(1024)
        if result == b"OK":
            file = open(filename, "wb")
            while 1:
                fdata = self.sock.recv(1024)
                if fdata == b"^&*":
                    print("下载成功！")
                    break
                file.write(fdata)
            file.close()  # 这里退出可以使缓存区里的数据出来
        else:
            print("请不要乱打")


# 图形展示 输入
class FTPView:
    def __init__(self):
        self.__ftp = FTPHandle()

    def __display_menu(self):
        print("")
        print("1) 查看文件")
        print("2) 上传文件")
        print("3) 下载文件")
        print("4) 退   出")
        print("")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == '1':
            self.__ftp.do_list()
        elif item == '2':
            filename = input("需下载的文件名")
            self.__ftp.do_upload(filename)
        elif item == '3':
            filename = input("需上传的文件名")
            self.__ftp.do_get(filename)
        elif item == '4':
            self.__ftp.do_quit()
        else:
            print("请输入正确选项！")

    # 入口程序启动
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


if __name__ == '__main__':
    ftpview = FTPView()
    ftpview.main()  # 启动
