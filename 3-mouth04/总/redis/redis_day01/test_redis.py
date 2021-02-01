import redis

# 创建redis数据库的连接对象
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
# 返回的值是字节
print(r.keys('*'))
# 判断键是否存在
print(r.exists('lst1'), r.exists('lst2'), r.exists('lst3'))
# 字节串操作
r.set('name', 'dewagfeagfae回答', 1234)
print(r.get('name').decode())
# 设置多个字符串的键值对时，用字典
print(r.mset({'a1': 12, 'b2': '12da', 'c3': 12312, 'd4': 'afgggggg', }))
print(r.mget(['a1', 'b2', 'c3', 'd4']))






