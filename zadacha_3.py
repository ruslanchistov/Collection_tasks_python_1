# Отсортируйте словарь по значению в порядке возрастания и убывания.

data = {'a':10,'b': 2,'c':8,'e':1,'d':5}

# Первый вариант:
# В порядке возрастания
list_1 = (sorted(data.values()))
data_1 ={}
for elem in list_1:
    for key,value in data.items():
        if elem == value:
            data_1.update({key:value})
print(data_1)

# В порядке убывания
list_1 = reversed((sorted(data.values())))
data_1 ={}
for elem in list_1:
    for key,value in data.items():
        if elem == value:
            data_1.update({key:value})
print(data_1)

# Второй вариант:
import operator
# В порядке возрастания
result = dict(sorted(data.items(),key=operator.itemgetter(1)))
print(result)

# В порядке убывания
result = dict(sorted(data.items(),key=operator.itemgetter(1),reverse=True))
print(result)