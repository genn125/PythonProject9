year = 2030
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
start_day = 3
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

def get_duration(year, month_index):
    if month_index in [3, 5, 8, 10]:
        duration = 30
    elif month_index == 1:
        duration = 29 if is_leap_year(year) else 28
    else:
        duration = 31
    return duration

def print_days(days_in_month, start_day):
    spases = ('   ' * start_day)
    print(spases, end='')
    for day in range(1, days_in_month + 1):    # Здесь вместо days подставьте диапазон.
        if day < 10:
            print(day, end='  ')
        else:
            print(day, end=' ')
        if (day + start_day)  % 7 == 0:
            print()

def print_header(year, month_index):   # Функция для вывода месяца и года
    print(months[month_index], year)  # вывод месяца и года
    print('Пн Вт Ср Чт Пт Сб Вс')

# Функция, вычисляющая день недели, который приходится на 1 января:(взята откуда то)
def get_starting_day(year):
    d = 1
    m = 13
    y = year - 1
    h = (d + (13 * (m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return (h + 5) % 7

# Функция, вычисляющая день недели,
# на который выпадет первое число следующего месяца:
def adjust_start_day(start_day, days_in_month):
    result = (start_day + days_in_month) % 7
    return result

# Вычисляем день недели, на который приходится 1 января года year:
start_day = get_starting_day(year)

# В цикле вызываем необходимые функции:
for month_number in range(12):
    print_header(year, month_number)   # вызов функции для вывода месяца и года
    duration = get_duration(year, month_number)
    print_days(duration, start_day)                           # Вызываем функцию и передаём в неё значение duration.

    # Переопределяем переменную start_day:
    start_day = adjust_start_day(start_day, duration)

    print()



