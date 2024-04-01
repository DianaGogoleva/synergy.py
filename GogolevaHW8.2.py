N = int(input('Введите количество элементов массива: '))
array = list(map(int, input('Введите числа через пробел: ').split()))
new_array = []
new_array.append(array[-1])
new_array.extend(array[:-1])

for element in new_array:
    print(element, end=' ')
