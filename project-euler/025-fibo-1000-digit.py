import fibo


def main():
    i = 1
    while True:
        f = fibo.fibo_series_dynamic(i)
        if len(str(f)) == 1000:
            print '1000 digit fibo is %s with index %s' % (f, i)
            break
        i += 1


if __name__ == "__main__":
    main()
