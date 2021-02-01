import csv
import os
import time

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from test_upload.models import Content


@cache_page(50)
def test_cache(request):
    t1 = time.time()
    print('-------------------------views in------------------')
    time.sleep(3)
    return HttpResponse(f'time is {t1}')


def test_mw(request):
    print('my view in')
    return HttpResponse('my middleware view!')


def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    if request.method == 'POST':
        username = request.POST['username']
        return HttpResponse(f'你的名字是{username}')


def test_page(request):
    # 1 要分页的数据
    list1 = ['1', '2', '3', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'giao', 'o', 'g']
    # 2 创建paginator对象
    paginator = Paginator(list1, 6)
    # 3 从查询字符串中获取当前页的页码
    cur_page = request.GET.get('page', 1)
    # 4 创建page对象
    page = paginator.page(cur_page)
    # 5 返回页面
    return render(request, 'test_page.html', locals())


def test_csv(request):
    # 1前两行固定代码
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    # 2 创建csv写入器
    writer = csv.writer(response)
    # 3写入标题
    writer.writerow(['图书编号', '图书名称'])
    # 准备数据
    all_books = [
        {'id': 1, 'title': 'giao'},
        {'id': 2, 'title': '我给你奶子一全'},
        {'id': 3, 'title': '吃我一棒'},
        {'id': 4, 'title': '啊！！！！'},
    ]
    # 写入数据
    for b in all_books:
        writer.writerow([b['id'], b['title']])
    return response


@csrf_exempt
def test_upload(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':
        # 获取文件对象
        afile = request.FILES['myfile']
        # 获取表单元素的值
        title = request.POST['title']
        # 第一种上传方法
        # # 生成一个服务器端文件的全路径
        # # GUID(全局唯一标识符)作为文件名的一部分防止重名
        # filename = os.path.join(settings.MEDIA_ROOT, afile.name)
        # with open(filename, 'wb') as f:
        #     #读取文件内容
        #     data = afile.file.read()
        #     #写入到服务器
        #     f.write(data)
        # result=f"文件{afile.name}上传成功，文件描述{title}"
        # return HttpResponse(result)
        # 第二种上传方法
        Content.objects.create(desc=title, myfile=afile)
        result = f"文件{afile.name}上传成功，文件描述{title}"
        return HttpResponse(result)
