from django.db import models
import random


def default_sign():
    signs = ['蜡笔小新', '百变小樱', '王路飞', 'giao', '彭于晏', '死变态', '高达', '柯南', '海王', '蜘蛛侠']
    return random.choice(signs)


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField('用户名', max_length=20, primary_key=True)
    nickname = models.CharField('昵称', max_length=50)
    email = models.EmailField('邮箱')
    password = models.CharField('密码', max_length=32)
    sign = models.CharField('个人签名', max_length=50, default=default_sign)
    info = models.CharField('个人简介', max_length=150, default='')
    avatar = models.ImageField(upload_to='avatar', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    phone = models.CharField('手机号', max_length=11, default='')
