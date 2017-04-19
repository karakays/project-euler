import itertools
import math


def trg_num_gen():
    for i in itertools.count(1):
        yield calc_triangle(i)


def calc_triangle_recrsv(nth):
    try:
        while nth > 1:
            return calc_triangle_recrsv(nth - 1) + nth
        return nth
    except RuntimeError as e:
        print e


def calc_triangle(nth):
    t = nth
    while nth:
        nth -= 1
        t += nth
    return t


def find_divisors_naive(num):
    divs = []
    for i in range(2, (num/2) + 1):
        if not num % i:
            divs.append(i)
    return divs


def find_divisors_paired(num):
    divs = []
    for i in range(1, int(math.ceil(num ** 0.5))):
        if not num % i:
            divs.extend([i, num/i])
    return divs


def main():
    gen = trg_num_gen()
    max = 1
    for t in gen:
        div_len = len(find_divisors_paired(t))
        if div_len > max:
            max = div_len
        print 'triangle is %s, %s. max until: %s' % (t, div_len, max)
        if div_len > 500:
            break


if __name__ == '__main__':
    main()
