f1=open("file.txt","wb+")
f1.write(b"wo cao ni ma")
p=f1.read(5)
print("gg",f1.tell())
f1.seek(-2, 2)
pp=f1.read()
print(pp)