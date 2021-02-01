"""质数:大于1的整数，除了1和它本身以外不能再被其他数字整除。
获取指定范围内所有质数。
"""

def giao(number):
    for i in range(2,number):
        if number%i==0:
            return False
        return True
def fiao(start,end):
    result=[]
    for i in range(start,end+1):
        if giao(i):
            result.append(i)

n1=int(input("来："))
n2=int(input("来："))
zresult=fiao(n1,n2)
print(zresult)

