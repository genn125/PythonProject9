year = 2030

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
          'Декабрь']

month_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

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


def print_header(year_value, month_index):
    print(year_value,months[month_index])
    duration = get_duration(year_value, month_index)
    print('Количество дней:', duration)

for month in month_numbers:
    print_header(year, month)




# Удалите эти вызовы функции и вместо них напишите цикл,
# который обработает список month_numbers
# и на каждой итерации будет вызывать функцию print_header(),
# поочерёдно подставляя во второй аргумент значения из списка: 0, 1, 2...
# print_header(year, 0)
# print_header(year, 1)
# print_header(year, 2)