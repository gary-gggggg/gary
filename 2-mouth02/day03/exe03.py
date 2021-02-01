title=open("file.txt","w")
title.write("《悯农》\n" )
title.close()
sum=0
while 1:
    sentence=open("file.txt","a")
    sum+=1
    if sum>4:
        sentence.close()
        break
    k =input("请输入句子（包括标点符号）：")
    sentence.write(f"{k}\n")
    sentence.close()

