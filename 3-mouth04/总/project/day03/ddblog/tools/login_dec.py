"""
登录用的装饰器
"""
import jwt
from django.http import JsonResponse
from django.conf import settings
from user.models import UserProfile


def login_check(func):
    def wrap(request, *args, **kwargs):
        # 在请求中获取前端提交过来的token
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 403, 'error': '请您先登录！'}
            return JsonResponse(result)
        # token 的校验
        try:
            payload = jwt.decode(token,
                                 settings.JWT_TOKEN_KEY,
                                 algorithm='HS256')
        except:
            result = {'code': 403, 'error': '请您先登录！'}
            return JsonResponse(result)
        # 从结果值获取私有声明
        username = payload['username']
        # 根据用户名称获取用户对象
        user = UserProfile.objects.get(username=username)
        # 将用户对象作为request的附加属性(只有python可以这样随意的添加)
        request.myuser = user
        # 调用所修饰的函数
        return func(request, *args, **kwargs)

    return wrap
