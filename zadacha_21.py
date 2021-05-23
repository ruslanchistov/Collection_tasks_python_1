# Задача 21
# Нужно проверить, все ли числа в последовательности уникальны.

import random
n = int(input('Введите количество элементов списка: '))
List = list(random.randint(1,200) for i in range(n))
print(List)

# Первый вариант
n = 0
for elem in List:
    n = List.count(elem)
    if n > 1:
        print('Не все числа уникальны !')
        break
if n <2 :
    print('Все числа уникальны')

# Второй вариант
if len(List) == len(set(List)):
    print('Все числа уникальны')
else:
    print('Не все числа уникальны !')