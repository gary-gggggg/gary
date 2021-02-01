"""练习：创建子类：狗(跑)，鸟类(飞)
创建父类：动物(吃)体会子类复用父类方法
体会 isinstance 、issubclass 与 type 的作用"""

class Animal:
    def eating(self):
        print("吃")

class Dog(Animal):
    def running(self):
        print("跑")

class Bird(Animal):
    def flying(self):
        print("飞")
A=Animal()
popy=Dog()
hiby=Bird()
print(isinstance(popy, Animal))
print(isinstance(popy,Dog))
print(isinstance(popy,Bird))
print(isinstance(hiby,Dog))
print(issubclass(Dog, Animal))
print(issubclass(Dog,Bird))
print(issubclass(Bird, Animal))
print(issubclass(Bird,Dog))
print(type(A) == Animal)
print(type(popy) == Dog)
print(type(Bird) == Animal)
print(type(Dog)==Bird)
