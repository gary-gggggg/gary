""" 在终端中累加 0  1  2  3
        在终端中累加 2  3  4  5  6
        在终端中累加 1  3  5  7
        在终端中累加 8  7  6  5  4
        在终端中累加 -1  -2  -3  -4  -5
"""
start = 2
c = 0
while start <= 6:
    # print(start) # 2 3
    c += start # 2 5
    start+=1 # 3
print(c)

start1=0
c1=0
while start1<=3:
    c1+=start1
    start1+=1
print(c1)

start1=1
c2=0
while start1<=7:
    c2+=start1
    start1+=2
print(c2)

start1=8
c3=0
while start1>=4:
    c3+=start1
    start1-=1
print(c3)

start1=-1
c4=0
while start1>=-5:
    c4+=start1
    start1-=1
print(c4)