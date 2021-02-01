import re
chuwenjian=open("log.txt","r+")
text=chuwenjian.read()
chuwenjian.close()
mingzi_list=re.findall(r"\n{2}(.+?) is",text)
for k in mingzi_list:
    if "Loopback" in k:
        mingzi_list.remove(k)
neirong_list=re.findall(r", address is (.+)", text)
def equipment(xx):
    sum=0
    for i in mingzi_list:
        sum+=1
        if xx == i:
         print(neirong_list[sum])
        break


mubiao=input("请输入设备名称：")
equipment(mubiao)











