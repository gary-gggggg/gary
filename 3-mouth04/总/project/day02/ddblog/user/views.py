import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import UserProfile
import hashlib
import time
import jwt
from django.conf import settings


# Create your views here.


class UserView(View):
    # 处理 v1/users的GET请求
    def get(self, request):
        return HttpResponse('-user get-')

    # 处理 v1/users的POST请求
    def post(self, request):
        # 1.获取前端给后端的json串
        json_str = request.body
        # 2.json串反序列化为对象
        json_obj = json.loads(json_str)
        # 3.从对象【字典】中获得数据
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password1 = json_obj['password_1']
        password2 = json_obj['password_2']
        # 4.数据检查
        # 4.1 检查注册的用户名是否可用
        old_client = UserProfile.objects.filter(username=username)
        old_email = UserProfile.objects.filter(email=email)
        if old_client:
            result = {'code': 10100, 'error': '该用户名已存在。'}
            return JsonResponse(result)
        if password1 != password2:
            result = {'code': 10101, 'error': '两次密码不一致。'}
            return JsonResponse(result)
        if old_email:
            result = {'code': 10102, 'error': '邮箱已被注册。'}
            return JsonResponse(result)

        # 4.3 添加密码的哈希值
        hash = hashlib.md5()
        hash.update(password1.encode())
        hpassword = hash.hexdigest()
        # 4.4 插入数据库(注意高并发！)
        try:
            user = UserProfile.objects.create(username=username,
                                              email=email,
                                              phone=phone,
                                              password=hpassword,
                                              created_time=time.time())

        except:
            return JsonResponse({'code': 10100, 'error': '该用户名已存在。'})
        else:
            # 使用token保持用户登录
            token = make_token(username)
            print(token)
            token = token.decode()  # 为啥要decode?
            # 这样就可以将生成的字节串转化为字符串
            return JsonResponse({'code': 200, 'username': username,
                                 'data': {'token': token}})


def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    return jwt.encode(payload, key, algorithm='HS256')
    # 使用官方（jwt）所给的encode用来生成token
