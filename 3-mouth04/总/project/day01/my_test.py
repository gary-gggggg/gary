import json
import base64
import time
import hmac
import copy


class Jwt():
    def __init__(self):
        pass

    # 生成token的方法
    @staticmethod
    def encode(payload, key, exp=300):
        """
        :param payload:载荷，token所承载的数据
        :param key: 共享的秘钥key
        :param exp: token以秒为单位的有效期。
        :return:一个二进制的token
        """
        # 1 初始化头
        # 1.1用字典表示header
        header = {'alg': 'HS256', 'typ': 'JWT'}
        # 1.2将字典序列化为json串
        hearder_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        # 键和值之间取消空格
        # sort_key是的原本无序的字典输出的结果变为有序
        # print(hearder_json)
        # 1.3 将json串(必须要以字节的形式)进行base64编码转换
        header_bs = Jwt.b64encode(hearder_json.encode())
        print(header_bs)
        # 2载荷（共有声明和私有声明）
        # 2.1对实参做一个深拷贝，不希望在函数内部修改到实参的值
        payload_data = copy.deepcopy(payload)
        # 2.2设置公有声明，token的有效期
        payload_data['exp'] = time.time() + int(exp)
        # 2.3对载荷对象字段序列化为json串
        payload_json = json.dumps(payload_data, separators=(',', ':'), sort_keys=True)
        # 2.4将json串转为base64
        payload_bs = Jwt.b64encode(payload_json.encode())
        print(payload_bs)
        # 签名(消息验证码的算法)
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        # 得到消息认证码
        digest = hm.digest()
        # 将消息认证码也要base64编码
        hm_bs = Jwt.b64encode(digest)
        print(hm_bs)
        return hm_bs + b'.' + payload_bs + b'.' + hm_bs

    @staticmethod
    def decode(token, key):
        """

        :param token:
        :param key:
        :return: 返回所需要的payload
        """
        # 拆分token的3部分
        hear_bs, payload_bs, sign = token.split(b'.')
        # 重新计算消息验证码
        hm = hmac.new(key.encode(), hear_bs + b'.' + payload_bs, digestmod='SHA256')
        # 得到消息认证码
        digest = hm.digest()
        # 将消息认证码也要base64编码
        sign2 = Jwt.b64encode(digest)
        # 1.两个消息认证码不相同，验证会失败
        if sign != sign2:
            raise
        # 2.将payloadbase解码得到json串，再反序列化
        # 一定要注意将去掉的等号补回来(def b64decode)
        payload_js = Jwt.b64decode(payload_bs)
        # 将json串反序列化为对象
        payload = json.loads(payload_js)
        exp = payload['exp']
        now = time.time()
        if now > exp:
            raise
        return payload

    @staticmethod
    def b64decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
            return base64.urlsafe_b64decode(b_s)

    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')


if __name__ == '__main__':
    token = Jwt.encode({'username': 'aid2010'},  # 私有声明
                       '123456',  # 共享秘钥
                       2)
    print(token)
    time.sleep(3)
    payload = Jwt.decode(token, '123456')
    print(payload)
