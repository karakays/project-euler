#!/usr/bin/env python3

import sys
from util.performance import log_performance as log_perform


def get_next_prime_number(n=2):
    def is_prime(i):
        if i == 2:
            return True
        for f in range(2, (i - 1)):
            if((i % f) == 0):
                return False
        return True

    while not is_prime(n):
        n += 1
    return n


def factorization_finished(l):
    return l.count(1) == len(l)


@log_perform
def find_lcm(numbers):
    lcm = []
    prime = get_next_prime_number()
    while not factorization_finished(numbers):
        factors = []
        for i, j in enumerate(numbers):
            if not (j % prime):
                numbers[i] = j // prime
                if prime not in factors:
                    factors.append(prime)
        lcm = lcm + factors
        if not len(factors):
            prime = get_next_prime_number(prime + 1)
    return lcm


def main():
    n = []
    for i in sys.argv[1:]:
        n.append(int(i))
    lcm = find_lcm(n)
    print(lcm)
    s = 1
    for c in lcm:
        s *= c
    print('Solution is {0}', s)


if __name__ == '__main__':
    main()
