# Задача 16
# Выведите список файлов в указанной директории.

from os import listdir
from os.path import isfile, join
files = [f for f in listdir('d:\Programm') if isfile(join('d:\Programm', f))]
print(files)