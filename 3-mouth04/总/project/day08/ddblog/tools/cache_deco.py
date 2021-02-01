from django.core.cache import cache

from tools.login_dec import get_user_by_request


def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request, *args, **kwargs):
            # 具体缓存的实现
            if 't_id' in request.GET.keys():
                return func(request, *args, **kwargs)
            # 是否是博主访问自己
            # 访问者名称
            visitor_name = get_user_by_request(request)
            # 作者名称
            author_id = kwargs['author_id']
            if visitor_name == author_id:
                cache_key = f'topic_cache_self_{request.get_full_path()}'
            else:
                cache_key = f'topic_cache_{request.get_full_path()}'
            print(f'----------cache key is {cache_key}----------')
            # 缓存思想：有缓存，访问缓存，没有缓存，调用函数，存入缓存
            res = cache.get(cache_key)
            if res:
                print('-----cache in ----')
                return res
            res = func(request, *args, **kwargs)
            cache.set(cache_key, res, expire)
            return res

        return wrapper

    return _topic_cache
