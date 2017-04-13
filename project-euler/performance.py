import time


def log(func):
    pass


def log_performance(func):
    def perform(*args):
        start = time.time()
        r = func(*args)
        print('%s() took %s seconds' % (func.__name__, (time.time() - start)))
        return r
    return perform
