def gggg(qq):
    fr = open(qq, "rb")
    fw = open("/home/tarena/ggg", "ab")
    while 1:
        o = fr.read(1024)
        if not o:
            break
        fw.write(o)


qq = input("请输入文件名：")
gggg(qq)
