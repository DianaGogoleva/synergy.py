import random

# Ввод размеров матрицы пользователем в формате rows * columns
rows, columns = map(int,input("Введите размер матрицы в формате 'строки * столбцы': ").split('*'))

# Генерация двух матриц rows x columns
matrix_1 = [[random.randint(-200,200) for _ in range(columns)] for _ in range(rows)]
matrix_2 = [[random.randint(-200,200) for _ in range(columns)] for _ in range(rows)]

# Создание новой матрицы для результата
matrix_3 = [[0 for _ in range(columns)] for _ in range(rows)]

# Сложение двух матриц
for i in range(rows):
    for j in range(columns):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

# Печать результата
print(matrix_3)
