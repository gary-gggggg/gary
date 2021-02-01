test06 = open("file.txt", "wb", buffering=10)
while 1:
    giao = input("//")
    if not giao:
        break
    test06.write(giao.encode())
