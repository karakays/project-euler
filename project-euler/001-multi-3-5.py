#!/usr/bin/env python

limit = 1000
res = 0


def foo():
    global res
    for i in xrange(limit):
        if not i % 3 or i % 5:
            res = res + i
    return res


def main():
    print foo()


if __name__ == '__main__':
    main()
