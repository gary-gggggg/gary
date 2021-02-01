import time

real_time = time.strftime("00. %Y年%m月%d日%y点:%m分:%S秒", time.localtime())
print(real_time)
giao=open("file.txt","w")
print(giao.write(real_time))
