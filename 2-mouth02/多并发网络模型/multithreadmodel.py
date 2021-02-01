"""
基于多线程的网络并发服务
重点代码 ！！
"""
from socket import *
from threading import Thread


# 具体处理客户端事务
class Handle:
    def request(self, data):
        print(data)


# 为每个客户端创建线程
class ClientThread(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        self.handle = Handle()
        super().__init__(daemon=True)

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data:
                break
            self.handle.request(data)
        self.connfd.close()


# 并发服务类
class ConcurrentServer:
    """
    提供并发服务
    """

    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self.__create_socket()

    # 创建套接字
    def __create_socket(self):
        tcp_socket = socket()
        tcp_socket.bind(self.address)
        return tcp_socket

    # 启动服务
    def serve_forever(self):
        print("Listen the port %d" % self.port)
        self.sock.listen(5)
        while True:
            connfd, addr = self.sock.accept()
            print("Connect from", addr)
            # 为客户端创建线程
            thread = ClientThread(connfd)
            thread.start()


if __name__ == '__main__':
    server = ConcurrentServer(host="0.0.0.0", port=8888)
    server.serve_forever()