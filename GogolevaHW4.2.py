x = float(input('Введите пятизначное число:'))
a = x % 10 # нашли единицы
b = (x - a) % 100 / 10 # нашли десятки
c = (x - (a+b*10)) % 1000 / 100 # нашли сотни
d = (x - (a+b*10+c*100)) % 10000 / 1000 # нашли тысячи
e = (x - (a+b*10+c*100+d*1000)) % 100000 / 10000 # нашли сотни тысяч
f = ((b ** a) * c) / (e - d)
print (f)