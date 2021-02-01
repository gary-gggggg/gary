import redis
import time

# 创建连接池并连接到redis
pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379, password='123456')
r = redis.Redis(connection_pool=pool)


def time_spend(fun):
    def giao(r, *args, **kwargs):
        t1 = time.time()
        fun(r)
        t2 = time.time()
        print(t2 - t1)

    return giao


@time_spend
def withpipeline(r):
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i + 1
        p.set(key, value)
    p.execute()


@time_spend
def withoutpipeline(r):
    for i in range(1000):
        key = 'test2' + str(i)
        value = i + 1
        r.set(key, value)


if __name__ == '__main__':
    withpipeline(r)
    withoutpipeline(r)










