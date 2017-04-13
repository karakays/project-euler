import math


def find_divisors(num):
    divs = []
    for i in range(1, int(math.ceil(num ** 0.5))):
        if not num % i:
            divs.extend([i, num/i])
    return divs
