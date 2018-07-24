# coding: utf-8

import time


class retry(object):
    def __init__(self, max_retries=3, wait=0, exceptions=(Exception,)):
        self.max_retries = max_retries
        self.exceptions = exceptions
        self.wait = wait

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.max_retries + 1):
                try:
                    result = func(*args, **kwargs)
                except self.exceptions:
                    print('retry', i)
                    time.sleep(self.wait)
                    continue
                else:
                    return result
        return wrapper


import random


@retry(5, 0.5, (ValueError, IndexError))
def foo():
    n = random.randint(-5, 5)
    if n < 0:
        raise ValueError('...')
    else:
        return n


x = foo()
print(x)
