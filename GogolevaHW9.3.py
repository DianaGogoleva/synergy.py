nums = list(map(int, input('Введите последовательность чисел: ').split(' ')))
seen = set()
for num in nums:
    if num in seen:
        print("YES")
    else:
        seen.add(num)
        print("NO")