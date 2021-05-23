# Напишите программу для слияния нескольких словарей в один.

a = {str(i):i**2 for i in range(5)}
b = {str(j):j**2 for j in range(5,9)}
print(a)
print(b)

# Первый вариант:
c = a
for key,value in b.items():
    c.update({key:value})
print(c)

# Второй вариант:
c = {}
for elem in (a,b):
    c.update(elem)
print(c)

# Третий вариант:
c = {**a,**b}
print(c)