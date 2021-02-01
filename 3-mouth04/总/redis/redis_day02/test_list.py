import redis

r = redis.Redis(host='localhost', port=6379, db=0, password='123456')
if __name__ == '__main__':
    r.flushdb()
    # 1、查看所有的键
    # 2、向列表 spider:urls 中以RPUSH放入如下几个元素：01_baidu.com、02_taobao.com、03_sina.com、04_jd.com、05_xxx.com
    # 3、查看列表中所有元素
    # 4、查看列表长度
    # 5、将列表中01_baidu.com 改为 01_tmall.com
    # 6、在列表中04_jd.com之后再加1个元素 02_taobao.com
    # 7、弹出列表中的最后一个元素
    # 8、删除列表中所有的 02_taobao.com
    # 9、剔除列表中的其他元素，只剩前3条
    print(r.rpush('spider:urls', '01_baidu.com', '02_taobao.com', '03_sina.com', '04_jd.com', '05_xxx.com'))
    print(r.lrange('spider:urls', 0, -1))
    print(r.llen('spider:urls'))
    print(r.lset('spider:urls', 0, '01_tmall.com'))
    print(r.linsert('spider:urls', 'after', "04_jd.com", '02_taobao.com'))
    print(r.rpop('spider:urls'))
    print(r.lrem('spider:urls', 0, '02_taobao.com'))
    print(r.ltrim('spider:urls', 0, 2))
    print(r.lrange('spider:urls', 0, -1))

