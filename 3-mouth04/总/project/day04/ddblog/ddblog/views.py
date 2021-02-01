from django.http import HttpResponse
from django.shortcuts import render


def test_cross(request):
    return render(request, 'test_cross.html')


def test_cross_server(request):
    return HttpResponse('我给你奶子一拳！！！')