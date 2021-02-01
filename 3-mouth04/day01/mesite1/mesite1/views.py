from django.http import HttpResponse


# 视图函数
# 参数为请求对象
# 返回值为响应对象
def page_2003(request):
    return HttpResponse('2003吊你吗')


def giao_314(request):
    return HttpResponse('我要睡觉了，不要叫我')


def page_index(request):
    return HttpResponse('你有了')


def page_number(requset, num):
    return HttpResponse(f'这是第{num}个giao')


def page_data(requeset, data):
    return HttpResponse(f'输入的内容是:{data}')


def page_cul(request, num1, op, num2):
    if op == 'add':
        return HttpResponse(num1 + num2)
    elif op == 'sub':
        return HttpResponse(num1 - num2)
    elif op == 'mul':
        return HttpResponse(num1 * num2)
    #测试request对象的使用，从request对象中获取客户端请求信息
    print(request.method)
    print(request.path_info)



def page_bir(requst,d,m,y):
    return HttpResponse(f'您的生日为{y}年{m}月{d}日')
