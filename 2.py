#
#
# a=[7, False, 4.4, 'ghj']
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
# c=a+b
# print('6 -', c)
# # print('7 -', a.__add__(b))
#

# a={}
# b=input('Введите ключ1: ')
# c=input('Введите значение1: ')
# b2=input('Введите ключ2: ')
# c2=input('Введите значение2: ')
# b3=input('Введите ключ3: ')
# c3=input('Введите значение3: ')
# a[b]=c
# a[b2]=c2
# a[b3]=c3
#
# # print(a)

#
# a = {3,567,8,467,6,8}
# a.add(57)
# b = {39586,57,57,767,8,0,-5}
# c = a & b
# print(list(c))
# print(c)


a={'q':1,'b':2,'c':[]}
a1=a.copy()  # Копирование через .copy() сохраняет ссылку на "с": [] и изменяет её в обоих объектах
a1['c'].append(3)
a1['c'].append(5)       #  {'q': 1, 'b': 2, 'c': [3, 5, 123]}
a['c'].append(123)      #  {'q': 1, 'b': 2, 'c': [3, 5, 123]}
print(a)
print(a1)

# from copy import deepcopy
# a={'q':1,'b':2,'c':[]}
# a1=deepcopy(a)  # Копирование через deepcopy(a) полностью копирует всё и изменяется всё НЕЗАВИСИМО
# a1['c'].append(3)
# a1['c'].append(5)      #  {'q': 1, 'b': 2, 'c': [123]}
# a['c'].append(123)     #  {'q': 1, 'b': 2, 'c': [3, 5]}
# print(a)
# print(a1)
# 