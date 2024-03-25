m = int(input('Укажите какой максимальный вес выдержит лодка: '))
n = int(input('Сколько рыбаков желает перебраться на тот берег: '))
fishermen = sorted([int(input('Сколько весит рыбак: ')) for _ in range(n)])
i, j = 0, n - 1
boats = 0
while i <= j:
    if fishermen[i] + fishermen[j] <= m:
        i += 1
        j -= 1
    else:
        j -= 1
    boats += 1
print(boats)