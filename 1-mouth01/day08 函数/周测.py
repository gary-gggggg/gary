"""斐波那契数列：从第三项开始，每项都等于前两项。
1,1,2,3,5,8,13,21..
根据长度获取斐波那契数列"""



def fibo(n):
    if n == 1:
        return ([1])
    if n == 2:
        return ([1, 1])
    else:
        res = [1, 1]
        for c in range(n - 2):
            az = res[-1] + res[-2]
            res.append(az)
        return (res)

long= int(input("请输入数列的长度："))
real_one=fibo(long)
print(real_one)
