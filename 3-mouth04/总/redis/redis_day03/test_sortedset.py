import redis

r = redis.Redis(password='123456')
r.flushdb()
r.zadd('zk1', {'giao1': 100, 'giao2': 90})
print(r.zrange('zk1', 0, -1, withscores=True))
r.zadd('zk2', {'giao2': 100, 'giao3': 80})
print(r.zrange('zk2', 0, -1, withscores=True))
r.zunionstore('zk3', ['zk1', 'zk2'], aggregate='sum')
print(r.zrange('zk3', 0, -1, withscores=True))
r.zunionstore('zk4', {'zk1': 0.3, 'zk2': 0.3, 'zk3': 0.4}, aggregate='min')
print(r.zrange('zk4', 0, -1, withscores=True))
