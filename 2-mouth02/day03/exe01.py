name1 = "file.txt"


def gerator():
    f1 = open(name1, "r")
    while True:
        p1 = f1.read(5)
        if p1 == "":
            f1.close()
            break
        yield p1


for k in gerator():
    print(k, end="")

