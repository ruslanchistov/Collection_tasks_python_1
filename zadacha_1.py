# Вывести элементы меньше пяти

# Первый вариант:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5 :
        print(i)

# Второй вариант:

import functools
print(list(filter(lambda i: i < 5,a)))

# Третий вариант:

print([i for i  in a if i < 5])