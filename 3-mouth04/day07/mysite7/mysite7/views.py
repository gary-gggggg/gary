import time

from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(50)
def test_cache(request):
    t1 = time.time()
    print('-------------------------views in------------------')
    time.sleep(3)
    return HttpResponse(f'time is {t1}')


def test_mw(request):
    print('my view in')
    return HttpResponse('my middleware view!')



