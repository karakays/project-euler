from util.primes import primes_sieve


def main():
    primes = primes_sieve(2000000)
    primes_sum = reduce((lambda x, y: x + y), primes)
    print 'Solution is %s' % primes_sum


if __name__ == '__main__':
    main()
