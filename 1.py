#Пользователь вводит нужный ему год, например - 2030
year = 2025

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

# Количество дней по месяцам:
days_in_month_0 = 31  # Январь.
days_in_month_1 = 29 if year % 4 == 0 else 28
days_in_month_2 = 31
days_in_month_3 = 30
days_in_month_4 = 31
days_in_month_5 = 30
days_in_month_6 = 31
days_in_month_7 = 31
days_in_month_8 = 30
days_in_month_9 = 31
days_in_month_10 = 30
days_in_month_11 = 31  # Декабрь.


# Исправьте функцию print_header() так, чтобы она принимала три параметра:
# год, название месяца и количество дней в месяце.
# В теле функции замените переменные months[1], year и days_in_month_1
# на названия соответствующих параметров.
def print_header(year_value,month_name,duration ):
    print(month_name,year_value)
    print('Количество дней:', duration)


# Ниже - два вызова функции print_header(). 
# Не изменяйте этот код: он поможет вам проверить работу.
print_header(year, months[0], days_in_month_0)
print_header(year, months[1], days_in_month_1)
