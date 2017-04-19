from util.factors import find_divisors


def find_proper_divisors(n):
    return [d for d in find_divisors(n) if d != n]


def sum_proper_divisors(n):
    return reduce(lambda x, y: x + y, find_proper_divisors(n), 0)


def is_ambicable(n):
    s = sum_proper_divisors(n)
    t = sum_proper_divisors(s)
    return n == t and n != s


def main():
    s = 0
    for i in range(1, 10000):
        if is_ambicable(i):
            s += i
    print s


if __name__ == "__main__":
    main()
