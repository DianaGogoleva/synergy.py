X = int(input('Введите натуральное число: '))
count = 0
i = 1
while i * i <= X:
    if X % i:
        i += 1
        continue
    if i * i == X:
        count += 1
    else:
        count += 2
    i += 1
print('Количество натуральных делитетй = ', count)
