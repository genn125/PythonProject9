


year = 2030

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


def is_leap_year(year):
    if year % 4 != 0:
        is_leap = False
    else:
        is_leap = True

    if year % 100 == 0:
        is_leap = False
    if year % 400 == 0:
        is_leap = True
    return is_leap


def get_duration(year_value, month_index):
    if month_index in [3, 5, 8, 10]:
        duration = 30
    elif month_index == 1:
        duration = 29 if is_leap_year(year_value) else 28
    else:
        duration = 31
    return duration


def print_days(days_in_month):
    for day in range(1, days_in_month + 1):
        if day < 10:
            print(day, end='  ')
        else:
            print(day, end=' ')
        if day % 7 == 0:
            print()

def print_header(year_value, month_index):
    print(months[month_index], year_value)
    print('Пн Вт Ср Чт Пт Сб Вс')

for month_number in range(12):
    print_header(year, month_number)
    duration = get_duration(year, month_number)
    print_days(duration)
    print()