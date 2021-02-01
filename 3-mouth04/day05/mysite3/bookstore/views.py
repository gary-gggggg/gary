from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book


# Create your views here.
def all_book(request):
    all_shit = Book.objects.all()
    return render(request, 'bookstore/all_book.html', locals())


def add_book(request):
    if request.method == 'GET':
        return render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        Book.objects.create(title=title, pub=pub, price=price, market_price=market_price)
        return HttpResponseRedirect('/bookstore/all_book')


def update_book(request, bid):
    try:
        i = Book.objects.get(id=bid)
    except:
        return HttpResponse('图片编号错误！')
    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        market_price1 = request.POST['market_price']
        pub1 = request.POST['pub']
        i.market_price = market_price1
        i.pub = pub1
        i.save()
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):
    did = request.GET.get('bid')
    # 获取要删除的对象
    try:
        book = Book.objects.get(id=did)
    except:
        return HttpResponse('图书编号错误！')
    book.delete()
    return HttpResponseRedirect('/bookstore/all_book')
