from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        if 'unames' in request.session and 'uid' in request.session:
            # 完成笔记功能后，重定向到笔记列表中
            return HttpResponse('您已经登录了')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取数据
        uname = request.POST['username']
        pwd = request.POST['pswd']
        # 数据检查
        if not uname or not pwd:
            return HttpResponse('用户名和密码不能为空！')
        try:
            user = User.objects.get(username=uname)
        except:
            return HttpResponse('用户名或密码不正确！')
        # 检查密码是否正确
        md5 = hashlib.md5()
        md5.update(pwd.encode())  # update()里要求是字节
        pwsd_hash = md5.hexdigest()  # 返回hash值
        if pwsd_hash != user.password:
            return HttpResponse('用户名或密码不正确！')
        # 使用session去保存登录状态
        request.session['unames'] = uname
        request.session['uid'] = user.id
        return HttpResponseRedirect('/note/')


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        uname = request.POST.get('username')
        pwd1 = request.POST.get('pswd1')
        pwd2 = request.POST.get('pswd2')
        if not uname or not pwd1 or not pwd2:
            return HttpResponse('请输入用户名和密码')
        if pwd1 != pwd2:
            return HttpResponse('两次密码需要一致')
        # 通过导包去验证用户名是否存在
        exist_user = User.objects.filter(username=uname)
        if exist_user:
            return HttpResponse('用户名已存在')
        # 数据入库前，为了安全，需要将密码转为hash值
        md5 = hashlib.md5()
        md5.update(pwd1.encode())  # update()里要求是字节
        pwsd_hash = md5.hexdigest()  # 返回hash值
        # 高并发可能会导致两个人重名，所以这里加个异常处理
        try:
            User.objects.create(username=uname, password=pwsd_hash)
        except:
            return HttpResponse('用户名已存在')
        return HttpResponse('register successfully')


def logout_view(request):
    if 'uname1' in request.session:
        del request.session['uname1']
    if 'uid' in request.session:
        del request.session['uid']
    return HttpResponse('quit successfully')
