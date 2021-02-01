import json
from alipay import AliPay
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.conf import settings

# 读取秘钥文件获取私钥和支付宝的公钥
app_private_key_string = open(settings.ALIPAY_KEY_DIR + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIR + 'alipay_public_key.pem').read()


# Create your views here.
class MyAliPay(View):
    def __init__(self, **kwargs):
        # 首先调用父类的构造函数
        super().__init__(**kwargs)
        # 创建alipay对象
        self.alipay = AliPay(
            # 应用id
            appid=settings.ALIPAY_APPID,
            # 接受结果的url
            app_notify_url=None,
            # 用户私钥
            app_private_key_string=app_private_key_string,
            # 支付宝公钥
            alipay_public_key_string=alipay_public_key_string,
            # 非对称加密算法
            sign_type='RSA2',
            # 制定调试/沙箱模式
            debug=True,

        )
        print(app_private_key_string)
        print(alipay_public_key_string)

    def get_trade_url(self, order_id, amount):
        base_url = 'https://openapi.alipaydev.com/gateway.do'
        # 根据参数生成订单的查询字符串
        order_string = self.alipay.api_alipay_trade_page_pay(
            # 1 订单编号
            out_trade_no=order_id,
            # 2 订单总金额
            total_amount=amount,
            # 3 订单标题
            subject=order_id,
            # 4 用户支付完成后，告知支付宝跳转到商家的哪个页面
            return_url=settings.ALIPAY_RETURN_URL,
            # 5 支付结果通知的url
            notify_url=settings.ALIPAY_NOTIFY_URL,

        )
        print(base_url + '?' + order_string)
        return base_url + '?' + order_string


class JumpView(MyAliPay):
    def get(self, request):
        return render(request, 'ajax_alipay.html')

    def post(self, request):
        print('1111111111111')
        json_str = request.body
        json_obj = json.loads(json_str)
        order_id = json_obj['order_id']
        # 生成并返回pay_url
        # 参数1：订单编号，参数2：订单金额
        # 编写一个父类对象，在构造函数中，初始化一个alipay对象
        # 调用alipay对象的相关方法完成功能
        pay_url = self.get_trade_url(order_id, 78888)
        return JsonResponse({'pay_url': pay_url})


# 订单状态
ORDER_STATUS = 1  # 未支付


class ResultView(MyAliPay):
    def get(self, request):
        # return HttpResponse('支付过程完成，跳转到该页面！，我giao！')
        # 当用户主动查询订单信息的时候
        request_data = {k: request.GET[k] for k in request.GET.keys()}
        # 从request_data里去获取订单编号
        order_id = request_data['out_trade_no']
        print(order_id)
        # 到底要不要主动查询
        # 如果支付过程完成了，但是数据库中的订单状态，任然是未支付
        if ORDER_STATUS == 1:
            # 服务器挂了，则需要注定查询
            result = self.alipay.api_alipay_trade_query(out_trade_no=order_id)
            if result.get('trade_status') == 'TRADE_SUCCESS':
                # 修改数据库的订单状态，将来支付修改为支付成功
                return HttpResponse('主动查询结果为：支付成功！')
            else:
                # 修改数据库的订单状态，将来支付修改为支付失败
                return HttpResponse('主动查询结果为：支付失败！')
        elif ORDER_STATUS == 2:
            return HttpResponse('支付成功！')
        elif ORDER_STATUS == 3:
            return HttpResponse('支付成功！')

    # 可能还有另外一个有ip地址的服务器，接受支付发送的post请求
    # 告知其支付结果
    def post(self, request):
        # 1 将request.POST这个类字典结构转换为字典结构
        request_data = {'k': request.POST[k] for k in request.POST.keys()}
        # 2 从post中取出支付宝的签名
        sign = request_data.pop('sign')
        # 3 验证签名
        is_verify = self.alipay.verify(request_data, sign)
        if is_verify:
            # 验证通过
            # 从request_data获取订单的支付状态
            trade_status = request_data['trade_status']
            if trade_status == 'TRADE_SUCCESS':
                # 若交易成功，则需要修改数据库中的状态，将来支付修改为1，支付完成改为2
                return HttpResponse('修改订单状态成功giao!!!')
        else:
            # 需要修改数据库中的状态,支付失败的话修改为3
            return HttpResponse('验签失败，请求不合法！giao!!!!')
