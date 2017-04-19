from 013_large_sum import sum_str_nums

LIMIT_POWER = 32


def power_str(power, base=2):
    if power <= LIMIT_POWER:
        return str(base ** power)
    limit = base ** LIMIT_POWER
    result_str = str(limit)
    rem_power = power - 32
    while(rem_power):
        result_str = sum_str_nums(result_str, result_str)
        rem_power -= 1
    return result_str


def main():
    res_str = power_str(1000)
    digit_sum = 0
    for n in res_str:
        digit_sum += int(n)
    print digit_sum


if __name__ == '__main__':
    main()
