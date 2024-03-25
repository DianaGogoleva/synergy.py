N = int(input('Введите количество чисел:'))
nums = list(map(int, input('Введите числа через пробел: ').split(' '))) 
res = []
for i in range(N):
    if i % 2 == 0:
        res.append(nums[-(i//2+1)])
    else:
        res.append(nums[i//2])
for num in res:
    print(num, end=" ")