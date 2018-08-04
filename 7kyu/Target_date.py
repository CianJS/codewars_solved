# -*- coding: utf-8 -*-

"""
ref: https://www.codewars.com/kata/target-date/
"""

def date_nb_days(a0, a, p):
    from datetime import datetime, timedelta
    default_date = datetime(2016, 1, 1)
    p /= 36000
    increasing_days = 0
    while a0 <= a:
        a0 *= (1 + p)
        increasing_days += 1
    default_date += timedelta(days=increasing_days)
    return default_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    print date_nb_days(4281, 5087, 2), "2024-07-03"