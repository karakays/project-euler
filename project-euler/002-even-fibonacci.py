#!/usr/bin/env python3.5

from util.performance import log_performance as log_perform

fibo_memoize = []


def fibo_series_recursive(elem):
    if elem == 0:
        return 0
    elif elem == 1:
        return 1

    return fibo_series_recursive(elem - 1) + fibo_series_recursive(elem - 2)


def fibo_series(limit):
    a = 0
    b = 1
    while(a + b < limit):
        yield(a + b)
        c = a
        a = b
        b = b + c


@log_perform
def fibo_series_even_sum_recursive(limit):
    sum = 0
    elem = 1
    while(True):
        x = fibo_series_recursive(elem)
        if x >= limit:
            return sum
        if not (x % 2):
            sum = sum + x
        elem = elem + 1


@log_perform
def fibo_series_even_sum(limit):
    sum = 0
    for i in fibo_series(limit):
        if not (i % 2):
            sum = sum + i
    return sum


def main():
    print('Answer with recursive is %s' %
            fibo_series_even_sum_recursive(4000000))
    print('Answer with generator is {0}'.format(fibo_series_even_sum(4000000)))


if __name__ == '__main__':
    main()
