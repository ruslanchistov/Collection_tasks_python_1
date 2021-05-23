# Задача 17
# Сложите цифры целого числа.

number = input('Введите число : ')
result = sum(int(i) for i in number)
print(result)
