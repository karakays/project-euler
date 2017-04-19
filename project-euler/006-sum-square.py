from functools import reduce

sum = lambda x, y: x + y


def square_sum(n):
    i = reduce(sum, n)
    return i * i


def sum_square(n):
    l = [i * i for i in n]
    return reduce(sum, l)


def main():
    i = square_sum(range(1, 101))
    j = sum_square(range(1, 101))
    print('Solutions is ', i - j)


if __name__ == '__main__':
    main()
