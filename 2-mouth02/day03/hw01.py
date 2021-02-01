import time
program=open("my.log","a+",buffering=1)
program.seek(0)
n=len(program.readlines())+1
while 1:
    real_time=time.strftime("%Y年%m月%d日 %y:%m:%S",time.localtime())
    program.write(f"{n}.{real_time}\n")
    n+=1
    time.sleep(2)




