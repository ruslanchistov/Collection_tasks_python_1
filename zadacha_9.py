# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

data = int(input('Введите количество секунд: '))
day = data//86400
chas = data % 86400 // 3600
min = data % 3600 // 60
sec = data % 60
print('Дни:',day)
print('Часы:',chas)
print('Mинуты:',min)
print('Секунды:',sec)
print(day,':',chas,':',min,':',sec)