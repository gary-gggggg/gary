import time


# 原始函数
def func():
    print('giao')
    time.sleep(1)
    print('gggg')


# 1：扩张函数功能，打印该函数执行的时间消耗
def func_ex():
    start_time = time.time()
    print('giao')
    time.sleep(1)
    print('gggg')
    end_time = time.time()
    timeout = end_time - start_time
    print(f'timeout is {timeout}')


# 2: 进一步的扩展函数功能【不修改原函数】,将函数作为参数传进来
def deco(func):
    start_time = time.time()
    func()
    end_time = time.time()
    timeout = end_time - start_time
    print(f'timeout is {timeout}')


# 3:使用装饰器【不修改原函数】,将函数作为参数传进来
# 比第二个的差别在于，这个会返回内部函数【函数编写嵌套，闭包】
# 参数：装饰器的参数是被修饰（被扩展功能）的函数
# 返回值： 返回内部函数【内部函数的作用扩展原有函数的功能】
def deco2(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        timeout = end_time - start_time
        print(f'timeout is {timeout}')

    # 返回内部函数
    return wrapper


@deco2
def func2():
    print('giao')
    time.sleep(1)
    print('gggg')


# 使用装饰器修饰带参数的函数
def deco3(func):
    def wrapper(a, b):
        start_time = time.time()
        func(a, b)
        end_time = time.time()
        timeout = end_time - start_time
        print(f'timeout is {timeout}')

    return wrapper


# 原始函数
@deco3
def func_param(a, b):
    print('函数的功能是求两个数值的和：')
    time.sleep(1)
    print(f'result is {a + b}')


# 使用装饰器去修饰带参数的函数，被修饰的参数个数不定
def deco4(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        timeout = end_time - start_time
        print(f'timeout is {timeout}')

    return wrapper


@deco4
def sum_two(a, b):
    print('两个数值的和:')
    time.sleep(1)
    print(f'a+b={a + b}')


@deco4
def sum_three(a, b, c):
    print('三个数值的和:')
    time.sleep(1)
    print(f'a+b+c={a + b + c}')


# 带参数的装饰器【装饰器带参数，需要定义三层装饰器】
def deco_param(expire):
    def dece_param2(func):
        def wrapper(second):
            start_time = time.time()
            print(f'expire is {expire}')
            func(second)
            end_time = time.time()
            timeout = end_time - start_time
            print(f'timeout is {timeout}')
        return wrapper
    return dece_param2
# 原始函数
@deco_param(10)
def func3(second):
    print('giao')
    time.sleep(second)
    print('gggg')


if __name__ == '__main__':
    # func2是有装饰器的，调用func2(),相当于调用deco2(func2)
    # 由于deco2返回wrapper函数，所以，相当与调用了内部函数的wrapper
    func3(3)
