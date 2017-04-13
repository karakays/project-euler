fact_memo = {0: 1, 1: 1}


def factorial_naive(n):
    if n == 1:
        return 1
    return n * factorial_naive(n - 1)


def factorial_opt(n):
    if fact_memo.get(n):
        return fact_memo[n]
    else:
        fact_memo[n] = n * factorial_opt(n - 1)
        return fact_memo[n]


def main():
    factorial_naive(100)
    n = factorial_opt(100)
    sum = reduce(lambda x, y: x + y, [int(s) for s in str(n)])
    print sum


if __name__ == "__main__":
    main()
