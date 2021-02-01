import json

from django.http import JsonResponse
from django.shortcuts import render

from message.models import Message
from tools.login_dec import login_check

# Create your views here.
# 0 发表评论时需要加登录认证
from topic.models import Topic
from user.models import UserProfile


@login_check
def message_view(request, topic_id):
    # 1 要限定前端发送的是post请求
    if request.method != 'POST':
        result = {'code': 10400, 'error': '请输入post请求'}
        return JsonResponse(result)
    # 2 从前端获取评论内容、parent_id、默认值为0
    json_str = request.body
    json_obj = json.loads(json_str)
    content = json_obj['content']
    parent_id = json_obj.get('parent_id',0)
    # 3 验证topic_id对应的文章是否存在，获取topic对象
    try:
        topic=Topic.objects.get(id=topic_id)
    except:
        result = {'code': 10401, 'error': '文章id错误'}
        return JsonResponse(result)
    # 4 从请求对象中获取用户对象
    user = request.myuser
    # 5 数据入库
    Message.objects.create(topic=topic,
                           content=content,
                           user_profile=user,
                           parent_message=parent_id)
    # 6 返回200
    return JsonResponse({'code': 200})
