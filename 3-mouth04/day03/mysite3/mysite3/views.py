from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index_view(request):
    return render(request, 'base.html')


def sports_veiw(request):
    return render(request, 'sports.html')


def sports_news(request):
    return render(request, 'news.html')


def pagen_views(request, n):
    print(reverse('pgn_url', args=[400]))
    return HttpResponse(f"this is {n} page")


def test_static(request):
    return render(request, 'test_static.html')


def index_view2(request):
    return render(request, 'index.html')
