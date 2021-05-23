# Задача 15
# Напишите программу, которая принимает два списка
# и выводит все элементы первого, которых нет во втором.

import random
n = int(input('Введите количество элементов первого списка: '))
m = int(input('Введите количество элементов второго списка: '))
list_1 = list(random.randint(1,100) for i in range(n))
list_2 = list(random.randint(1,100) for i in range(m))
list_3 = list(i for i in list_1 if i not in list_2)
print(list_1)
print(list_2)
print(list_3)