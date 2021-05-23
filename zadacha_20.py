# Задача 20
# С помощью анонимной функции извлеките из списка числа, делимые на 15.

import random
n = int(input('Введите количество элементов списка: '))
List = list(random.randint(1,500) for i in range(n))
result = list(filter(lambda i: not i%15,List))
print(result)