from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def test_xhr(request):
    return render(request, 'test_xhr.html')


def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')


def test_xhr_get_server(request):
    return HttpResponse('我给你奶子一拳 ajax data')


def test_jq_get(request):
    return render(request, 'test_jq_get.html')


def test_json(request):
    return render(request, 'test_json.html')


def make_json_server(request):
    # dict1 = {'name': 'gary', "age": 19}
    # return JsonResponse(dict1)
    list1 = [
        {'name': 'gary', "age": 19},
        {'name': 'xavier', "age": 89}
    ]
    # 因为是列表所以要加flase
    return JsonResponse(list1, safe=False)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        print(uname, pwd)
        return HttpResponse(f'{uname} ok ')


def test_cross(request):
    return render(request, 'cross.html')


def cross_server(request):
    # 获取预留函数的名称
    func = request.GET.get('callback')
    # 范湖数据时数据需要使用函数名包起来
    # func('我跨域来了')
    return HttpResponse(f"{func}('我跨域来了')")
