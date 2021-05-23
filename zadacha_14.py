# Задача 14
# Напишите программу, которая выводит чётные числа из заданного списка
# и останавливается, если встречает число 237.

import random
n = int(input('Введите количество элементов списка : '))
data = list(random.randint(1,500) for i in range(n))
print(data)
date = []
for idx,i in enumerate(data):
    if i % 2 == 0:
        date.append(i)
    if i == 237:
        print('Есть точка останова',idx,'-й элемент')
        break
print(date)