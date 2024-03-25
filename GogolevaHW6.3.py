A = int(input('Введите число A, которое <= B: '))
B = int(input('Введите число B, которое >= A: '))
for i in range(A, B+1):
    if i % 2 == 0:
        print( i, end=" ")