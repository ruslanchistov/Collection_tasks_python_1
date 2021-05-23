# Задача 18
# Посчитайте, сколько раз символ встречается в строке.

stroka = input('Введите строку : ')
simbol = input('Введите искомый символ : ')
List = list(stroka)
rezult = List.count(simbol)
print(simbol,'встречается',rezult,'раз(а)')