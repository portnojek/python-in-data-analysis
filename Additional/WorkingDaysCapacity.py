import math
from datetime import date, timedelta, datetime
from workalendar.europe import Poland

year = 2025
capacity_office = 0.4
cal = Poland()

def count_working_days_with_holidays(year, month, holiday_dates):
    first_day = date(year, month, 1)
    if month == 12:
        last_day = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = date(year, month + 1, 1) - timedelta(days=1)

    working_days = 0
    current_day = first_day
    while current_day <= last_day:
        if current_day.weekday() < 5 and current_day not in holiday_dates:
            working_days += 1

        current_day += timedelta(days=1)

    return working_days

months = [datetime(year, i, 1).strftime('%B') for i in range(1, 13)]
def count_working_days_year(year):
    holidays = cal.holidays(year)
    holiday_dates = {day for day, name in holidays}

    working_days_per_month = {}
    forty_percent_per_month = {}
    total_working_days = 0
    total_forty_percent = 0

    for month in range(1, 13):
        month_name = months[month-1]
        workking_days = count_working_days_with_holidays(year, month, holiday_dates)
        forty_percent = math.ceil(workking_days * capacity_office)
        working_days_per_month[month] = workking_days
        forty_percent_per_month[month] = forty_percent
        total_working_days += workking_days
        total_forty_percent += forty_percent
        print(f"{month_name} {year}: {workking_days} dni roboczych, z tego {round(capacity_office*100)}% ro {forty_percent} dni")

    return month_name, working_days_per_month, forty_percent_per_month, total_working_days, total_forty_percent

month_name, working_days_per_month, forty_percent_per_month, total_working_days, total_forty_percent = count_working_days_year(year)

print(f"\nŁączna liczba dni roboczych w roku {year}: {total_working_days}")
print(f"Łączna liczba dni w biurze w roku {year}: {total_forty_percent}")