#1.1
import numpy as np
N = int(input("Введите размерность матрицы N: "))
A = np.random.randint(-10, 10, (N, N))
print("Матрица A:\n", A)
sum_positive = 0
count_positive = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i][j] > 0:
            sum_positive += A[i][j]
            count_positive += 1
print("Сумма положительных элементов:", sum_positive)
print("Количество положительных элементов:", count_positive)
#1.2
M = int(input("Введите количество столбцов M: "))
B = np.random.randint(-10, 10, (N, M))
print("Матрица B:\n", B)
for i in range(N):
    max_index = np.argmax(B[i])
    min_index = np.argmin(B[i])
    B[i][max_index], B[i][0] = B[i][0], B[i][max_index]  # Меняем местами с первым элементом
    B[i][min_index], B[i][-1] = B[i][-1], B[i][min_index]  # Меняем местами с последним элементом
print("Измененная матрица B:\n", B)
#2.1
def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False
    return True
n = int(input("Введите размерность матрицы n: "))
matrix = np.random.randint(1, 10, (n, n))
print("Матрица:\n", matrix)
print("Является ли магическим квадратом:", is_magic_square(matrix))
#2.2
N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))
A = np.random.randint(-10, 10, (N, M))
print("Исходная матрица A:\n", A)
A[:, [0, -1]] = A[:, [-1, 0]]
print("Матрица после перестановки:\n", A)
#3.1
def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T)
n = int(input("Введите размерность матрицы n: "))
matrix = np.random.randint(-10, 10, (n, n))
print("Матрица:\n", matrix)
print("Является ли симметричной:", is_symmetric(matrix))
#3.2
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))
matrix = np.random.rand(n, m)
print("Исходная матрица:\n", matrix)
max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
matrix[0, 0], matrix[max_index] = matrix[max_index], matrix[0, 0]

print("Матрица после перемещения максимального элемента:\n", matrix)
#4.1
N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))
A = np.random.randint(-10, 10, (N, M))
print("Матрица A:\n", A)
row_sums = A.sum(axis=1)
max_row_index = np.argmax(row_sums)
min_row_index = np.argmin(row_sums)
print("Строка с максимальной суммой:", A[max_row_index], "Сумма:", row_sums[max_row_index])
print("Строка с минимальной суммой:", A[min_row_index], "Сумма:", row_sums[min_row_index])

#4.2
N = int(input("Введите размерность матрицы N: "))
A = np.random.randint(-10, 10, (N, N))
print("Исходная матрица A:\n", A)
A[A < 0] = 0
A[A > 0] = 1
lower_triangle = np.tril(A)
print("Нижняя треугольная матрица:\n", lower_triangle)
#5.1
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))
matrix = np.random.randint(-10, 10, (n, m))
print("Исходная матрица:\n", matrix)
sorted_matrix = np.sort(matrix, axis=1)
print("Отсортированная матрица:\n", sorted_matrix)
#5.2
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))
matrix = np.random.rand(n, m)
print("Исходная матрица:\n", matrix)
new_matrix = matrix.copy()
for i in range(n):
    min_value_index = np.argmin(new_matrix[i])
    if new_matrix[i][min_value_index] % 2 == 0:
        new_matrix[i][min_value_index] = 0
    else:
        new_matrix[i][min_value_index] = 1
print("Новая матрица:\n", new_matrix)
#6.1
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))
matrix = np.random.randint(-10, 10, (n, m))  # Пример случайной матрицы
print("Матрица:\n", matrix)

max_in_rows = np.max(matrix, axis=1)
min_in_cols = np.min(matrix, axis=0)

print("Наибольшие элементы в строках:", max_in_rows)
print("Наименьшие элементы в столбцах:", min_in_cols)

#6.2
N = int(input("Введите размерность матрицы N (нечетное): "))
matrix = np.random.rand(N, N)
print("Исходная матрица:\n", matrix)
main_diag_max = np.max(np.diag(matrix))
secondary_diag_max = np.max(np.diag(np.fliplr(matrix)))
max_value = max(main_diag_max, secondary_diag_max)
if max_value == main_diag_max:
    main_diag_indices = [(i, i) for i in range(N)]
    index_of_max_value = main_diag_indices[np.argmax(np.diag(matrix))]
    intersection_index = (N // 2, N // 2)
    matrix[index_of_max_value], matrix[intersection_index] = matrix[intersection_index], matrix[index_of_max_value]
    print(f"Максимальный элемент на главной диагонали перемещен на пересечение: {matrix}")
#7.1
import numpy as np
def restore_symmetric_matrix(upper_triangle):
    n = int((np.sqrt(1 + 8 * len(upper_triangle)) - 1) / 2)
    matrix = np.zeros((n, n))
    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[index]
            matrix[j][i] = upper_triangle[index]
            index += 1
    return matrix
upper_triangle_array = [1, 2, 3, 4, 5, 6, 7]
restored_matrix = restore_symmetric_matrix(upper_triangle_array)
print("Восстановленная симметричная матрица:")
print(restored_matrix)
#7.2
import numpy as np
n = int(input("Введите размерность квадратной матрицы N: "))
matrix = np.random.randint(1, 10, (n, n))
print("Исходная матрица:")
print(matrix)
diagonal_elements = [matrix[i][i] for i in range(n)]
trace_of_matrix = sum(diagonal_elements)
transformed_matrix = matrix.copy()
for i in range(n):
    if i % 2 == 0:
        transformed_matrix[i] /= trace_of_matrix
print("След матрицы:", trace_of_matrix)
print("Преобразованная матрица:")
print(transformed_matrix)
#8.1
import numpy as np
n = int(input("Введите количество строк и столбцов n: "))
k = int(input("Введите номер строки k (0-indexed): "))
matrix = np.random.randint(-10, 10, (n, n))
print("Исходная матрица:")
print(matrix)
if k < 0 or k >= n:
    print("Ошибка: номер строки k вне диапазона.")
else:
    diagonal_element_k_row = matrix[k][k]
    if diagonal_element_k_row != 0:
        matrix[k] = matrix[k] / diagonal_element_k_row
    print(f"Матрица после деления k-й строки на диагональный элемент:")
    print(matrix)










