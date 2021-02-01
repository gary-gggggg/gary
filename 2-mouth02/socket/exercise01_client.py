from socket import *

# 记录服务端地址
ADDR = ("127.0.0.1", 8888)


class QueryWord:
    def __init__(self):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 发送单词得到解释
    def find_word(self, word):
        self.udp_socket.sendto(word.encode(), ADDR)
        data, addr = self.udp_socket.recvfrom(1024)
        return data.decode()

    # 输入和输入控制
    def query_word(self):
        while True:
            # 将输入的单词发送给服务端
            word = input("\n要查询的单词：")
            # 客户端直接退出
            if not word:
                break
            mean = self.find_word(word)
            print("%s : %s" % (word, mean))

    def close(self):
        self.udp_socket.close()


if __name__ == '__main__':
    query = QueryWord()
    query.query_word() # 请求查单词
    query.close()
