import time


def caching(timeout):
    _caches = {}

    def func_wrapper(func):

        def inner():
            func_name = func.__name__

            if func_name in _caches:
                cache, func_timeout, time_of_adding = _caches[func_name]
                if time.time() - time_of_adding < func_timeout:
                    return cache
                else:
                    _caches.pop(func_name)

            cache = func()
            _caches[func_name] = cache, timeout, time.time()
            return cache

        return inner

    return func_wrapper
