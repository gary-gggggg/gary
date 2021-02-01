import json
from topic.models import Topic
from django.http import JsonResponse, request
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from tools.login_dec import login_check, get_user_by_request

# Create your views here.
from user.models import UserProfile


class TopicView(View):
    @method_decorator(login_check)
    def post(self, request, author_id):
        # 1 从请求对象的附加数据中获取用户对象
        author = request.myuser
        # 2 从前端获取用户输入的值（内容，不带格式的内容，权限，分类，标题）
        json_str = request.body
        json_obj = json.loads(json_str)
        content = json_obj['content']
        introduce = json_obj['content_text'][:20]
        title = json_obj['title']
        limit = json_obj['limit']
        category = json_obj['category']
        # 3 检查分类的值一定是tec或no-tec
        # 4 检查权限一定是public或private
        if category not in ['tec', 'no-tec']:
            result = {'code': 10300, 'error': '分类错误！'}
            return JsonResponse(result)
        if limit not in ['public', 'private']:
            result = {'code': 10301, 'error': "权限错误！"}
            return JsonResponse(result)
        # 5 数据入库
        Topic.objects.create(title=title,
                             content=content,
                             limit=limit,
                             category=category,
                             introduce=introduce,
                             user_profile=author)
        return JsonResponse({'code': 200, 'username': author.username})

    def get(self, request, author_id):
        pass
        # 1 分类的思考
        # v1/topics/XXX  #所有分类
        # v1/topics/XXX?category=tec/no-tec #技术/非技术文章列表
        # 权限的思考
        # 登录用户访问自己的文章，可以访问所有的文章（包括public+private）
        # 游客或者非作者本人访问别人的文章，只能访问public的文章
        # 需要区分开访问者是不是作者本人

        # 获取文章的作者这个对象
        try:
            author = UserProfile.objects.get(username=author_id)
        except:
            result = {'code': 10305, 'error': '用户名称错误！'}
            return JsonResponse(result)
        # 获取访问者的身份（有可能是游客，有可能是登录用户）
        visitor_name=get_user_by_request(request)
