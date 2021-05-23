# Нужно вывести первые n строк треугольника Паскаля.
# В этом треугольнике на вершине и по бокам стоят единицы,
# а каждое число внутри равно сумме двух расположенных над ним чисел.

# Первый вариант:
def func_1(n):
    result = [1]
    current = [0]
    while n > 0:
        print(result)
        cur_result = list(zip(result + current, current + result))
        result = []
        for tpl in cur_result:
            result.append(tpl[0] + tpl[1])
        n -= 1

# Второй вариант:
def func_2(n):
    result = [1]
    for i in range(n):
        print(result)
        res = [1]
        for j in range(len(result)-1):
            res.append(result[j] + result[j + 1])
        res.append(1)
        result = res

# Третий вариант:
def pascal(n):
    row = [1]
    y = [0]
    for x in range(max(n,0)):
        print(row)
        row = [left + right for left, right in zip(row + y,y + row)]

n = int(input('Введите количество строк : '))
func_1(n)
func_2(n)
pascal(n)