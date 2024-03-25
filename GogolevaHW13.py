import random

# Генерация двух матриц 10x10
matrix_1 = [[random.randint(-200,200) for _ in range(10)] for _ in range(10)]
matrix_2 = [[random.randint(-200,200) for _ in range(10)] for _ in range(10)]

# Создание новой матрицы для результата
matrix_3 = [[0 for _ in range(10)] for _ in range(10)]

# Сложение двух матриц
for i in range(10):
    for j in range(10):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

# Печать результата
print(matrix_3)
print(matrix_3)