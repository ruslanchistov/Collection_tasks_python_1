# Задача 22
# Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное.

# Первый вариант
text = input('Введите текст : ')
list_text = text.split()
max_count = 0
max_str =''
max_long = 0
for elem in list_text:
    cur_count = list_text.count(elem)
    cur_long = len(elem)
    if cur_long > max_long:
        cur_long = max_long
        long_str = elem
    if cur_count > max_count:
        max_count = cur_count
        max_str = elem
print('Слово: ',max_str,'  число повторов: ',max_count)
print('Самое длинное слово: ',long_str)

#Второй вариант
import collections

counter = collections.Counter(list_text)
most_common, occurrences = counter.most_common()[0]

longest = max(list_text, key=len)

print(most_common, longest)