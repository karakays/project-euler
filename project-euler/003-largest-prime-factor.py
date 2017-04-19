import sys


def prime_factors(n):
    l = []
    i = 2
    while i <= n:
        if not (n % i):
            n = n / i
            l.append(i)
        else:
            i += 1
    return l


def next_prime_factor(n):
    i = 2
    while i <= n:
        if not (n % i):
            yield i
            n = n / i
        else:
            i += 1


def is_prime(i):
    for f in range(2, (i - 1)):
        if not (i % f):
            return False
    return True


def main():
    n = int(sys.argv[1])
    print(is_prime(n))
    print(prime_factors(n))
    for i in (next_prime_factor(n)):
        print(i)


if __name__ == '__main__':
    main()
