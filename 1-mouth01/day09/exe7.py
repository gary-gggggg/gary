"""练习：说出程序执行结果.
def func01(list_target):
print(list_target)# ?
def func02(*args):# 三合一
print(args)# ?
def func03(*args,**kwargs):# 三合一
print(args)# ?
print(kwargs)# ?
def func04(p1,p2,*,p4,**kwargs): print(p1)# 10
print(p2)# 20
print(p4)# 30
print(kwargs)# {p5 : 40}
func01([1,2,3])
func02(*[1,2,3])# 一拆三
func03(1,2,3,a=4,b=5,c=6)
func04(10,20,p4 = 30,p5 = 40)"""