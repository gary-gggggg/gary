from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import redis

r = redis.Redis(password='123456')


# Create your views here.
def user_detail(request, uid):
    chache_key = f'user_{uid}'
    if r.exists(chache_key):
        # 读取缓存数据
        data = r.hgetall(chache_key)
        new_data = {k.decode(): v.decode() for k, v in data.items()}
        print(new_data)
        username = new_data['username']
        age = new_data['age']
        result = f'cache:username is {username},age is {age}'
        return HttpResponse(result)
    else:
        try:
            user = User.objects.get(id=uid)
        except:
            return HttpResponse('用户id错误')
        # 写入缓存，为下一次访问提供方便
        r.hmset(chache_key, {'username': user.username, 'age': user.age})
        # 设置缓存的有效期
        r.expire(chache_key, 50)
        # 返回响应
        result = f'mysql:username is {user.username},age is {user.age}'
        return HttpResponse(result)


def user_update(request, uid):
    # 查询字符串获取年龄
    age = request.GET.get('age', 18)
    # 1 查
    try:
        user = User.objects.get(id=uid)
    except:
        return HttpResponse('用户ID有误！')
    # 2 改
    user.age = age
    # 3 保存
    user.save()
    # 清理缓存
    chache_key = f'user_{uid}'
    r.delete(chache_key)
    return HttpResponse('更新用户年龄成功!')
