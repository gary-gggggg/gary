from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response


# class MyMiddleWare2(MiddlewareMixin):
#     def process_request(self, request):
#         K = request.META['REMOTE_ADDR']
#         v = ip_dict.get(f'{K}', 'none')
#         if v == 'none':
#             ip_dict[f'{K}']=1
#         if v<=5:
#             v+=1
#     def process_view(self, request, callback, callback_args, callback_kwargs):
#         print("中间件方法 process_view 被调用")
#
#     def process_response(self, request, response):
#         print("中间件方法 process_response 被调用")
#         return response

class MyMiddleWare3(MiddlewareMixin):
    visit_name = {}

    def process_request(self, request):
        cip = request.META['REMOTE_ADDR']
        # 只有path以/test开头的才做次数限制
        if not re.match(r'^/test', request.path_info):
            return
        times = self.visit_name.get(cip, 0)
        if times >= 5:
            return HttpResponse('no way!')
        self.visit_name[cip] = times+1
        print(f"{cip}visit{times}times")
