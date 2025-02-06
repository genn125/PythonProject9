#
#
# a=[7, False, 4.4, 'ghj']
#
# a.pop(1)
# a.pop(2)
# a.sort()
# print('1 -', a)
# print('2 -', len(a))
# a[1:3] = ['Привет', 'Мир']     # заменил
# print('3 -', a)
# a[1:3] = a[1:3][::-1]        # Переставил
# print('4 -', a)
# b=[4565,68.67]
# a.extend(b)
# print('5 -', a,b)
#
# c=a+b
# print('6 -', c)
# print('7 -', a.__add__(b))

a={}

b=input('Введите ключ1: ')
c=input('Введите значение1: ')
b2=input('Введите ключ2: ')
c2=input('Введите значение2: ')
b3=input('Введите ключ3: ')
c3=input('Введите значение3: ')
a[b]=c
a[b2]=c2
a[b3]=c3

print(a)
