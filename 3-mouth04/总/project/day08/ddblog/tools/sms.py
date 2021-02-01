import datetime
import hashlib
import base64
import json
import requests  # 使用该库发送请求


class YunTongXin():
    base_url = 'https://app.cloopen.com:8883'

    def __init__(self, accountSid, accountToken, appId, templateId):
        self.templateId = templateId
        self.appId = appId
        self.accountToken = accountToken
        self.accountSid = accountSid

    # 构造url
    def get_request_url(self, sig):
        self.url = self.base_url + f'/2013-12-26/Accounts/{self.accountSid}/SMS/TemplateSMS?sig={sig}'
        return self.url

    # 生成时间戳
    def get_timestamp(self):
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        return now_str

    # 计算sig
    def get_sig(self, timestamp):
        data = self.accountSid + self.accountToken + timestamp
        md5 = hashlib.md5()
        md5.update(data.encode())
        hash_value = md5.hexdigest()
        return hash_value.upper()

    # 2 构造请求头
    def get_request_header(self, tiemstamp):
        data = self.accountSid + ":" + tiemstamp
        data_bs = base64.b64encode(data.encode())
        data_bs = data_bs.decode()
        return {'Accept': 'application/json',
                'Content-Type': 'application/json;charset=utf8',
                'Authorization': data_bs}

    # 3 构造请求体
    def get_request_body(self, phone, code):
        data = {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            'datas': [code, '3']
        }
        return data

    # 4 发送请求
    def do_request(self, url, header, body):
        res = requests.post(url, headers=header,
                            data=json.dumps(body))
        return res.text  # 里面有个text属性,我们只看那个

    # 5 封装意思所有函数
    def run(self, phone, code):
        # 1 构建url
        timestamp = self.get_timestamp()
        sig = self.get_sig(timestamp)
        url = self.get_request_url(sig)
        # 2 构建header
        header = self.get_request_header(timestamp)
        # 3 构建body
        body = self.get_request_body(phone, code)
        # 4 发送请求
        res = self.do_request(url, header, body)
        return res


if __name__ == '__main__':
    ACCOUNT_SID = "8a216da877373e59017741b591970551"
    AUTH_TOKEN = "4a683bb3d59a44da860f1b3ef1836652"
    AppID = "8a216da877373e59017741b592550557"
    tid = '1'
    # 1创建云通信对象
    x = YunTongXin(ACCOUNT_SID, AUTH_TOKEN, AppID, tid)
    # 2发送通信
    res = x.run('13516717227', '123456')
    # 3 打印返回信息
    print(res)

