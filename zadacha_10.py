# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.

data = input('Введите числа через запятую : ')
data_list = list(int(i) for i in data.split(','))
print(type(data_list),data_list)
data_tuple = tuple(data_list)
print(type(data_tuple),data_tuple)