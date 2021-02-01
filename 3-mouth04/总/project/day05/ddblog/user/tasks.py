from ddblog.celery import app
from tools.sms import YunTongXin
from django.conf import settings


@app.task
def send_sms(phone, code):
    # 1创建云通信对象
    x = YunTongXin(settings.ACCOUNT_SID, settings.AUTH_TOKEN, settings.APP_ID, settings.TID)
    # 2发送通信
    res = x.run(phone, code)
    # 3 打印返回信息
    print(res)
