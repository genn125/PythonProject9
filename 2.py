


days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

print('Пн Вт Ср Чт Пт Сб Вс')

def print_days():
    for day in days:
        if day < 10:
           print (day, end="  ")
        else:
           print(day, end=" ")
        if day % 7 == 0:
            print('')
print_days()