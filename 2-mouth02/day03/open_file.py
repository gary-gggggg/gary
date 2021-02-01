file=open("dict.txt",'r')
key=[]
value=[]
for k in file:
    tmp=k.split(" ")
    key.append(tmp[0])

    value.append(tmp[1])



print(value)




