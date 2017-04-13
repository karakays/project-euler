fibo_memoize = {1: 1, 2: 1}


def fibo_series(nth):
    if not nth:
        return 1
    elif nth == 1:
        return 1
    else:
        return fibo_series(nth -1) + fibo_series(nth - 2)


def fibo_series_dynamic(nth):
    if fibo_memoize.get(nth):
        return fibo_memoize[nth]
    else:
        fibo_memoize[nth] = fibo_series_dynamic(nth - 1) + fibo_series_dynamic(nth - 2)
        return fibo_memoize[nth]
