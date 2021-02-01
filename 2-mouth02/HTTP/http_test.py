"""获取http请求和响应"""
from socket import *

filename = "/home/tarena/FTP/ggg.jpg"
s = socket()
s.bind(('0.0.0.0', 4658))
s.listen(5)

c, addr = s.accept()
print(f"收到:{addr}")

data = c.recv(1024)
print("receive:", data.decode())
file = open(filename, "rb")
response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:image/jpeg\r\n"
response += "\r\n"
response=response.encode()+file.read()
c.send(response)
file.close()
c.close()
s.close()
