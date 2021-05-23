# Программа считает количество строк, слов и букв в переданном ей файле.

file_name = 'zadacha_23.txt'
stroka = 0
slovo = 0
simbol = 0
file = open(file_name,'r')
for line in file:
    stroka += 1
    simbol += len(line)
    slovo += len(line.split())
file.close()
print('strok : ',stroka)
print('slov : ',slovo)
print('simbolov : ',simbol)
