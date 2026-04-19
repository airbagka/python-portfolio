import random

matrix = [[random.randint(1, 99) for _ in range(4)] for _ in range(4)]

print("Матрица 4x4:")
for row in matrix:
    print("  " + "  ".join(f"{x:2d}" for x in row))

row_sums = [sum(row) for row in matrix]
print(f"Суммы строк: {row_sums}")

col_sums = [sum(matrix[i][j] for i in range(4)) for j in range(4)]
print(f"Суммы столбцов: {col_sums}")

diag_sum = sum(matrix[i][i] for i in range(4))
print(f"Сумма главной диагонали: {diag_sum}")
