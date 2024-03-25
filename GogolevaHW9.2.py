list1 = set(map(int, input('Введите первый список чисел: ').split(' ')))
list2 = set(map(int, input('Введите второй список чисел: ').split(' ')))
print(len(list1.intersection(list2)))
