import json
import random
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse, JsonResponse
from tools.sms import YunTongXin
from .models import UserProfile
import hashlib
import time
import jwt
from django.conf import settings
from tools.login_dec import login_check
from django.core.cache import cache


# Create your views here.


class UserView(View):
    # 处理 v1/users的GET请求
    def get(self, request, username=None):
        if username:
            # 如果username存在则是返回制定用户的信息
            try:
                user = UserProfile.objects.get(username=username)
            except:
                result = {'code': 10104, 'error': '用户名称错误!'}
                return JsonResponse(result)
            if request.GET.keys():
                # 获取指定信息
                data = {}
                for k in request.GET.keys():
                    if k == 'password':
                        continue
                    if hasattr(user, k):
                        data[k] = getattr(user, k)
                result = {'code': 200, 'username': username, 'data': data}
            else:
                # 按格式返回制定用户的全量信息
                result = {'code': 200, 'username': username,
                          'data': {'info': user.info, 'sign': user.sign,
                                   'nickname': user.nickname,
                                   'avatar': str(user.avatar)}}
            return JsonResponse(result)
        else:
            return HttpResponse('-返回所有用户信息-')

    # 处理 v1/users的POST请求(为什么这里不用写username形参)
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
        # 获取验证码
        sms_num = json_obj['sms_num']  # 这是个字符串
        cache_key = f'sms_{phone}'
        code = cache.get(cache_key)
        # 校对验证码
        if not code:
            result = {'code': 10110, 'error': '验证码已经过期'}
            return JsonResponse(result)
        if int(sms_num) != code:
            result = {'code': 10111, 'error': '验证码错误'}
            return JsonResponse(result)
        # 从缓存中获取验证码
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
                                              nickname=username,
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

    # /v1/users/用户名的put请求
    @method_decorator(login_check)
    def put(self, request, username):
        # 1 获取前端传过来的json串
        json_str = request.body
        # 2 将串转为对象
        json_obj = json.loads(json_str)
        # 3 获取要修改的用户
        user = request.myuser
        # 4 修改
        user.sign = json_obj['sign']
        user.nickname = json_obj['nickname']
        user.info = json_obj['info']
        # 5 保存
        user.save()
        # 返回
        result = {'code': 200, 'username': user.username}
        return JsonResponse(result)


def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    return jwt.encode(payload, key, algorithm='HS256')
    # 使用官方（jwt）所给的encode用来生成token


# 对用户信息的修改，头像的上传一定是需要登录认证才能操作。另外，其他操作也是：文章的操作等等
# 所以既然这么多东西都需要登录认证，所以直接搞装饰器（放到一个通用的tool里面）
@login_check
def user_avatar(request, username):  # 虽然不用这个username但是还是必须要写这个形参
    if request.method != 'POST':
        result = {'code': 10105, 'error': '只接受post请求'}
        return JsonResponse(result)
    # 从request对象中获取已经登录的用户
    user = request.myuser
    # 修改用户头像
    user.avatar = request.FILES['avatar']
    # 保存
    user.save()
    # 返回
    result = {'code': 200, 'username': user.username}
    return JsonResponse(result)


# 使用redis去储存短信验证码
# django+redis更好
def sms_views(request):
    # 1 获取前端提交的数据
    json_str = request.body
    # 2 json串转为对象
    json_obj = json.loads(json_str)
    # 3获得手机号
    phone = json_obj['phone']
    # 4 生成随机的验证码
    code = random.randint(100000, 999999)
    # 5 将验证码存进缓存（redis)
    cache_key = f'sms_{phone}'
    cache.set(cache_key, code, 180)
    print(phone, code)
    # 6 向指定的手机号发送短信验证请求
    # 1创建云通信对象
    x = YunTongXin(settings.ACCOUNT_SID, settings.AUTH_TOKEN, settings.APP_ID, settings.TID)
    # 2发送通信
    res = x.run(phone, code)
    # 3 打印返回信息
    print(res)
    return JsonResponse({'code': 200})
