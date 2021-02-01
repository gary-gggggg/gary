import json
import hashlib
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from user.views import make_token

from user.models import UserProfile


class TokenView(View):
    def post(self, request):
        # 1.获得前端传递的json串
        json_str = request.body
        # 2.将json串转化为对象
        json_obj = json.loads(json_str)
        # 3.获取用户名和密码
        username = json_obj['username']
        password = json_obj['password']
        print(password)
        # 4.校验用户名和密码
        try:
            user = UserProfile.objects.get(username=username)
        except:
            result = {'code': 10200, 'error': '用户名或密码错误！'}
            return JsonResponse(result)
        md5 = hashlib.md5()
        md5.update(password.encode())
        hpassword = md5.hexdigest()
        if hpassword != user.password:
            result = {'code': 10201, 'error': '用户名或密码错误！'}
            return JsonResponse(result)
        # 5.校验完成后，签发token
        token = make_token(username)
        print(token)
        token = token.decode()
        return JsonResponse({'code': 200, 'username': username,
                             'data': {'token': token}})
