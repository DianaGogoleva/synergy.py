N = int(input('Укажите сколько чисел вы хотите ввести: '))
count = 0
for _ in range(N):
    if int(input('Введите число:')) == 0:
        count += 1
print(count)