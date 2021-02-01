from django.http import HttpResponse
from django.shortcuts import render
from .tasks import task_test
import datetime


# Create your views here.
def test_celery(request):
    # 推送任务后，马上返回。异步操作
    task_test.delay()
    # 不使用生产者消费者模式，同步执行
    # task_test()
    now = datetime.datetime.now()
    html = 'return at %s' % (now.strftime('%H:%M:%S'))
    return HttpResponse(html)
