import math
from datetime import date, timedelta, datetime
from workalendar.europe import Poland
import calendar
import tkinter as tk
from tkinter import ttk

year = 2026
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

def create_calendar_gui(year):
    root = tk.Tk()
    root.title(f"Calendar {year}")

    style = ttk.Style(root)
    style.theme_use('clam')  # Użyj motywu 'clam' dla lepszej kompatybilności
    style.configure("Holiday.TLabel", background="red", foreground="white")
    style.configure("WorkDay.TLabel", background="green", foreground="white")
    style.configure("Weekend.TLabel", background="gray", foreground="white")

    holidays = cal.holidays(year)
    holiday_dates = {day for day, name in holidays}

    for month in range(1, 13):
        frame = ttk.Frame(root, padding="3 3 12 12")
        frame.grid(row=(month-1)//3, column=(month-1)%3, sticky=(tk.N, tk.W, tk.E, tk.S))
        ttk.Label(frame, text=calendar.month_name[month]).grid(column=0, row=0, columnspan=7)

        for i, day in enumerate(["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]):
            ttk.Label(frame, text=day).grid(column=i, row=1)

        cal_month = calendar.monthcalendar(year, month)
        for week_num, week in enumerate(cal_month, 2):
            for day_num, day in enumerate(week):
                if day != 0:
                    date_obj = date(year, month, day)
                    if date_obj in holiday_dates:
                        style_name = "Holiday.TLabel"
                    elif date_obj.weekday() >= 5:
                        style_name = "Weekend.TLabel"
                    else:
                        style_name = "WorkDay.TLabel"
                    label = ttk.Label(frame, text=str(day), style=style_name)
                    label.grid(column=day_num, row=week_num, padx=1, pady=1)
                    label.configure(width=2, anchor="center")

    root.mainloop()

month_name, working_days_per_month, forty_percent_per_month, total_working_days, total_forty_percent = count_working_days_year(year)

print(f"\nŁączna liczba dni roboczych w roku {year}: {total_working_days}")
print(f"Łączna liczba dni w biurze w roku {year}: {total_forty_percent}")

create_calendar_gui(year)
