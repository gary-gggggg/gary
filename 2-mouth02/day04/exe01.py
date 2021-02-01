"""文件处理函数"""
import os
print("文件高管：",os.path.getsize("../day03/wife.jpg"))
print("文件类别：",os.listdir("."))
print("xx",os.path.isfile("../day03/wife.jpg"))
print("xxx",os.path.exists("giao"))
os.remove("../day03/my.log")