import math
from datetime import date, timedelta, datetime
from workalendar.europe import Poland
import calendar
import tkinter as tk

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
        month_name = months[month - 1]
        workking_days = count_working_days_with_holidays(year, month, holiday_dates)
        forty_percent = math.ceil(workking_days * capacity_office)
        working_days_per_month[month] = workking_days
        forty_percent_per_month[month] = forty_percent
        total_working_days += workking_days
        total_forty_percent += forty_percent
        print(
            f"{month_name} {year}: {workking_days} dni roboczych, z tego {round(capacity_office * 100)}% to {forty_percent} dni")

    return month_name, working_days_per_month, forty_percent_per_month, total_working_days, total_forty_percent


def create_calendar_gui(year, working_days_per_month, forty_percent_per_month):
    root = tk.Tk()
    root.title(f"Calendar {year}")

    holidays = cal.holidays(year)
    holiday_dates = {day for day, name in holidays}

    for month in range(1, 13):
        frame = tk.Frame(root, padx=5, pady=5, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=(month - 1) // 3, column=(month - 1) % 3, sticky=(tk.N, tk.W, tk.E, tk.S), padx=5, pady=5)

        month_name = calendar.month_name[month]
        tk.Label(frame, text=f"{month_name} {year}", font=('Arial', 12, 'bold')).grid(column=0, row=0, columnspan=7)

        for i, day in enumerate(["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]):
            tk.Label(frame, text=day, font=('Arial', 8)).grid(column=i, row=1)

        cal_month = calendar.monthcalendar(year, month)
        for week_num, week in enumerate(cal_month, 2):
            for day_num, day in enumerate(week):
                if day != 0:
                    date_obj = date(year, month, day)
                    if date_obj in holiday_dates:
                        bg_color = "red"
                    elif date_obj.weekday() >= 5:
                        bg_color = "gray"
                    else:
                        bg_color = "green"
                    label = tk.Label(frame, text=str(day), bg=bg_color, fg="white", width=2)
                    label.grid(column=day_num, row=week_num, padx=1, pady=1)

        # Dodajemy informacje o dniach roboczych i dniach w biurze
        work_days = working_days_per_month[month]
        office_days = forty_percent_per_month[month]
        info_text = f"Dni robocze: {work_days}\nDni w biurze: {office_days}"
        tk.Label(frame, text=info_text, font=('Arial', 8), justify=tk.LEFT).grid(column=0, row=8, columnspan=7,
                                                                                 sticky=tk.W)

    root.mainloop()


# Główna część programu
month_name, working_days_per_month, forty_percent_per_month, total_working_days, total_forty_percent = count_working_days_year(
    year)

print(f"\nŁączna liczba dni roboczych w roku {year}: {total_working_days}")
print(f"Łączna liczba dni w biurze w roku {year}: {total_forty_percent}")

create_calendar_gui(year, working_days_per_month, forty_percent_per_month)
