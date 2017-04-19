def coroutine(func):
    def wrapper(*args, **kwargs):
        w = func()
        w.next()
        return w
    return wrapper
