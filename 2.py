

a=[7, False, 4.4, 'ghj']

a.pop(1)
a.pop(2)
a.sort()
print(a)
print(len(a))
a[1:3] = ['Привет', 'Мир']     # заменил
print(a)
a[1:3] = a[1:3][::-1]        # Переставил
print(a)