# Найдите три ключа с самыми высокими значениями в словаре

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

# Первый вариант:
import operator

max_elem =dict(sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True))
i = 0
for  key,value in max_elem.items():
    if i <3:
        print(key,'-',value)
        i +=1

# Второй вариант:

max_elem=sorted(my_dict,key=my_dict.get,reverse=True)[:3]
print(max_elem)

# Третий вариант:

from heapq import nlargest

max_elem = nlargest(3,my_dict , key = my_dict.get)
print(max_elem)