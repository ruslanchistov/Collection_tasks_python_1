# Выведите первый и последний элемент списка.
import random
data_list = [random.randint(1,50) for i in range(1,11)]
print(data_list)
print('Первый элемент : ',data_list[0])
print('Последний элемент : ',data_list[-1])