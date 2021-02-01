import redis

r = redis.Redis(password='123456')
# 测试前清库
r.flushdb()
# 2 操作hash
r.hset('giao1', 'name', '小啊giao')
print(r.hget('giao1', 'name').decode())
r.hmset('giao1', {'age': 15, 'city': '杭州'})
print(r.hgetall('giao1'))
print(r.hvals('giao1'))
print(r.hkeys('giao1'))

