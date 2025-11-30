import numpy as np
with open('variant_1_vvod.txt', 'r') as vvod, open('variant_1_vivod.txt', 'w') as vivod:
    # 1.1
    lines = vvod.readlines()
    current_line = 0
    N = int(lines[current_line].strip())
    current_line += 1
    A = []
    for i in range(N):
        row = list(map(int, lines[current_line].split()))
        A.append(row)
        current_line += 1
    A = np.array(A)
    vivod.write("Матрица A:\n" + str(A) + "\n")
    sum_positive = 0
    count_positive = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] > 0:
                sum_positive += A[i][j]
                count_positive += 1
    vivod.write("Сумма положительных элементов: " + str(sum_positive) + "\n")
    vivod.write("Количество положительных элементов: " + str(count_positive) + "\n")
    # 1.2
    M = int(lines[current_line].strip())
    current_line += 1
    B = []
    for i in range(N):
        row = list(map(int, lines[current_line].split()))
        B.append(row)
        current_line += 1
    B = np.array(B)
    vivod.write("Матрица B:\n" + str(B) + "\n")
    for i in range(N):
        max_index = np.argmax(B[i])
        min_index = np.argmin(B[i])
        B[i][max_index], B[i][0] = B[i][0], B[i][max_index]
        B[i][min_index], B[i][-1] = B[i][-1], B[i][min_index]
    vivod.write("Измененная матрица B:\n" + str(B) + "\n")
    # 2.1
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
    n = int(lines[current_line].strip())
    current_line += 1
    matrix = []
    for i in range(n):
        row = list(map(int, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Матрица:\n" + str(matrix) + "\n")
    vivod.write("Является ли магическим квадратом: " + str(is_magic_square(matrix)) + "\n")
    # 2.2
    N = int(lines[current_line].strip())
    current_line += 1
    M = int(lines[current_line].strip())
    current_line += 1
    A = []
    for i in range(N):
        row = list(map(int, lines[current_line].split()))
        A.append(row)
        current_line += 1
    A = np.array(A)
    vivod.write("Исходная матрица A:\n" + str(A) + "\n")
    A[:, [0, -1]] = A[:, [-1, 0]]
    vivod.write("Матрица после перестановки:\n" + str(A) + "\n")
    # 3.1
    def is_symmetric(matrix):
        return np.array_equal(matrix, matrix.T)
    n = int(lines[current_line].strip())
    current_line += 1
    matrix = []
    for i in range(n):
        row = list(map(int, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Матрица:\n" + str(matrix) + "\n")
    vivod.write("Является ли симметричной: " + str(is_symmetric(matrix)) + "\n")
    # 3.2
    n = int(lines[current_line].strip())
    current_line += 1
    m = int(lines[current_line].strip())
    current_line += 1
    matrix = []
    for i in range(n):
        row = list(map(float, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Исходная матрица:\n" + str(matrix) + "\n")
    max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
    matrix[0, 0], matrix[max_index] = matrix[max_index], matrix[0, 0]
    vivod.write("Матрица после перемещения максимального элемента:\n" + str(matrix) + "\n")
    # 4.1
    N = int(lines[current_line].strip())
    current_line += 1
    M = int(lines[current_line].strip())
    current_line += 1
    A = []
    for i in range(N):
        row = list(map(int, lines[current_line].split()))
        A.append(row)
        current_line += 1
    A = np.array(A)
    vivod.write("Матрица A:\n" + str(A) + "\n")
    row_sums = A.sum(axis=1)
    max_row_index = np.argmax(row_sums)
    min_row_index = np.argmin(row_sums)
    vivod.write(
        "Строка с максимальной суммой: " + str(A[max_row_index]) + " Сумма: " + str(row_sums[max_row_index]) + "\n")
    vivod.write(
        "Строка с минимальной суммой: " + str(A[min_row_index]) + " Сумма: " + str(row_sums[min_row_index]) + "\n")
    # 4.2
    N = int(lines[current_line].strip())
    current_line += 1
    A = []
    for i in range(N):
        row = list(map(int, lines[current_line].split()))
        A.append(row)
        current_line += 1
    A = np.array(A)
    vivod.write("Исходная матрица A:\n" + str(A) + "\n")
    A[A < 0] = 0
    A[A > 0] = 1
    lower_triangle = np.tril(A)
    vivod.write("Нижняя треугольная матрица:\n" + str(lower_triangle) + "\n")
    # 5.1
    n = int(lines[current_line].strip())
    current_line += 1
    m = int(lines[current_line].strip())
    current_line += 1
    matrix = []
    for i in range(n):
        row = list(map(int, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Исходная матрица:\n" + str(matrix) + "\n")
    sorted_matrix = np.sort(matrix, axis=1)
    vivod.write("Отсортированная матрица:\n" + str(sorted_matrix) + "\n")
    # 5.2
    n = int(lines[current_line].strip())
    current_line += 1
    m = int(lines[current_line].strip())
    current_line += 1
    matrix = []
    for i in range(n):
        row = list(map(float, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Исходная матрица:\n" + str(matrix) + "\n")
    new_matrix = matrix.copy()
    for i in range(n):
        min_value_index = np.argmin(new_matrix[i])
        if new_matrix[i][min_value_index] % 2 == 0:
            new_matrix[i][min_value_index] = 0
        else:
            new_matrix[i][min_value_index] = 1
    vivod.write("Новая матрица:\n" + str(new_matrix) + "\n")
    # 6.1
    n = int(lines[current_line].strip())
    current_line += 1
    m = int(lines[current_line].strip())
    current_line += 1
    matrix = []
    for i in range(n):
        row = list(map(int, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Матрица:\n" + str(matrix) + "\n")
    max_in_rows = np.max(matrix, axis=1)
    min_in_cols = np.min(matrix, axis=0)
    vivod.write("Наибольшие элементы в строках: " + str(max_in_rows) + "\n")
    vivod.write("Наименьшие элементы в столбцах: " + str(min_in_cols) + "\n")
    # 6.2
    N = int(lines[current_line].strip())
    current_line += 1
    matrix = []
    for i in range(N):
        row = list(map(float, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Исходная матрица:\n" + str(matrix) + "\n")
    main_diag_max = np.max(np.diag(matrix))
    secondary_diag_max = np.max(np.diag(np.fliplr(matrix)))
    max_value = max(main_diag_max, secondary_diag_max)
    if max_value == main_diag_max:
        main_diag_indices = [(i, i) for i in range(N)]
        index_of_max_value = main_diag_indices[np.argmax(np.diag(matrix))]
        intersection_index = (N // 2, N // 2)
        matrix[index_of_max_value], matrix[intersection_index] = matrix[intersection_index], matrix[index_of_max_value]
        vivod.write(f"Максимальный элемент на главной диагонали перемещен на пересечение: \n{matrix}\n")
    # 7.1
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
    upper_triangle_array = list(map(float, lines[current_line].split()))
    current_line += 1
    restored_matrix = restore_symmetric_matrix(upper_triangle_array)
    vivod.write("Восстановленная симметричная матрица:\n" + str(restored_matrix) + "\n")
    # 7.2
    n = int(lines[current_line].strip())
    current_line += 1
    matrix = []
    for i in range(n):
        row = list(map(int, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Исходная матрица:\n" + str(matrix) + "\n")
    diagonal_elements = [matrix[i][i] for i in range(n)]
    trace_of_matrix = sum(diagonal_elements)
    transformed_matrix = matrix.copy()
    for i in range(n):
        if i % 2 == 0:
            transformed_matrix[i] /= trace_of_matrix
    vivod.write("След матрицы: " + str(trace_of_matrix) + "\n")
    vivod.write("Преобразованная матрица:\n" + str(transformed_matrix) + "\n")
    # 8.1
    n = int(lines[current_line].strip())
    current_line += 1
    k = int(lines[current_line].strip())
    matrix = []
    for i in range(n):
        row = list(map(int, lines[current_line].split()))
        matrix.append(row)
        current_line += 1
    matrix = np.array(matrix)
    vivod.write("Исходная матрица:\n" + str(matrix) + "\n")
    if k < 0 or k >= n:
        vivod.write("Ошибка: номер строки k вне диапазона.\n")
    else:
        diagonal_element_k_row = matrix[k][k]
        if diagonal_element_k_row != 0:
            matrix[k] = matrix[k] / diagonal_element_k_row
        vivod.write(f"Матрица после деления k-й строки на диагональный элемент:\n{matrix}\n")