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
###########################################################################

# a={'q':1,'b':2,'c':[]}
# a1=a.copy()             # Копирование через .copy() сохраняет ссылку на "с": [] и изменяет её в обоих объектах
# a1['c'].append(3)
# a1['c'].append(5)       #  {'q': 1, 'b': 2, 'c': [3, 5, 123]}
# a['c'].append(123)      #  {'q': 1, 'b': 2, 'c': [3, 5, 123]}
# print('1 -',a)
# print('2 -',a1)
#
#
# from copy import deepcopy
# a={'q':1,'b':2,'c':[]}
# a1=deepcopy(a)         # Копирование через deepcopy(a) полностью копирует всё и изменяется всё НЕЗАВИСИМО
# a1['c'].append(3)
# a1['c'].append(5)      #  {'q': 1, 'b': 2, 'c': [123]}
# a['c'].append(123)     #  {'q': 1, 'b': 2, 'c': [3, 5]}
# print('3 -',a)
# print('4 -',a1)
# ###############################################################################
# #
#
# def  merge_lists_to_dict(list_one, list_two):
#     return list_one+list_two
# print('1 -', merge_lists_to_dict(list_two=59,list_one=35, ))
# print('2 -', merge_lists_to_dict(50,list_two=35 ))
# print('3 -', merge_lists_to_dict(['a',True,100],['abc']))
# # 1 - 94
# # 2 - 85
# # 3 - ['a', True, 100, 'abc']
#
# def update_car_info(**car):
#
#     car["is_available"] = True
#     return car
#
# print('4 -', update_car_info(brand='BMW', price=100000))
# 4 - {'brand': 'BMW', 'price': 100000, 'is_available': True}

#
# print(update_car_info('BMW', 100000))
# # # TypeError: update_car_info() takes 0 positional arguments but 2 were given
# #######################################################################################
# #
# a = {2,4,6,8,9,0}
# b = {2,8,9,4,6,0}
# print('Равны ли значения переменных - ', a==b)  # True
# print('Равны ли адреса переменных - ',  is b)  # False
# print(id(a))
# print(id(b))
#
# print(9 in a)   # True
# print(9999 in b)  #  False
# print([]in a)   # TypeError: unhashable type: 'list'
###############################################################

def greeting(greet):

    # global info
    # def info(name):
    #     return  f'{greet}, {name}!'
    # return info
    return lambda name: f'{greet}, {name}!'

rr = greeting('good morning')


print(rr('Genn125'))
print(rr(1))

yy = greeting('Привет')
print(yy ('Genn125'))

