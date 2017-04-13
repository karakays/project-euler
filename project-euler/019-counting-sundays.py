def thirty_one_days(year=None):
    return 31


def thirty_days(year=None):
    return 30


days_in_month = {
        0: thirty_one_days,
        1: lambda(y): 29 if is_leap_year(y) else 28,
        2: thirty_one_days,
        3: thirty_days,
        4: thirty_one_days,
        5: thirty_days,
        6: thirty_one_days,
        7: thirty_one_days,
        8: thirty_days,
        9: thirty_one_days,
        10: thirty_days,
        11: thirty_one_days
}


def is_leap_year(year):
    if not (year % 100):
        return not (year % 400)
    return not (year % 4)


def get_days_in_month(month, year=None):
    return days_in_month[month](year)


def pass_time(day, month, year, weekday):
    sunday_count = 0
    while year <= 2000:
        while month <= 11:
            while get_days_in_month(month, year) >= day + 7:
                day += 7
            weekday = (weekday + get_days_in_month(month, year) - day + 1) % 7
            month = month + 1
            day = 1
            if weekday == 6 and year != 1900:
                sunday_count += 1
        month = 0
        year += 1
    print sunday_count


pass_time(1, 0, 1900, 0)
