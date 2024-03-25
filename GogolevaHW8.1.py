N = int(input('Введите колличество чисел и строк:'))
nums = []
for _ in range(N):
    nums.append(int(input('Введите числа:')))
nums.reverse()
for num in nums:
    print(num)