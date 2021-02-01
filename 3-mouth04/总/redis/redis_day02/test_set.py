import redis

r = redis.Redis(password='123456')
r.flushdb()
r.sadd('武将', '张飞', '赵云', '马超', '周瑜')
r.sadd('文臣', '周瑜', '诸葛亮', '司马懿', '郭嘉')
r.sdiffstore('纯武将', '武将', '文臣')
r.sdiffstore('纯文臣', '文臣', '武将')
r.sinterstore('文武双全', '文臣', '武将')
r.sunionstore('文臣武将', '文臣', '武将')
list_all=[]
for i in r.smembers('纯武将'):
    list_all.append(i.decode())
print(list_all)