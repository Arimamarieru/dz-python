import random


def generate_matrix(rows: int,
                    cols: int,
                    low: int = -100,
                    high: int = 100,
                    seed: int | None = None) -> list[list[int]]:
    if seed is not None:
        random.seed(seed)

    return [[random.randint(low, high) for _ in range(cols)]
            for _ in range(rows)]


def add_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
   
    rows, cols = len(a), len(a[0])
    return [[a[i][j] + b[i][j] for j in range(cols)]
            for i in range(rows)]


def print_matrix(m: list[list[int]], title: str = "Matrix") -> None:
   
    print(f"\n{title} ({len(m)} × {len(m[0])}):")
    for row in m:
        print("  ", row)


if __name__ == "__main__":
    rows = int(input("Сколько строк в матрице?  "))
    cols = int(input("Сколько столбцов?        "))
    low  = int(input("Нижняя граница диапазона случайных чисел: "))
    high = int(input("Верхняя граница диапазона случайных чисел: "))
  
    matrix_1 = generate_matrix(rows, cols, low, high)
    matrix_2 = generate_matrix(rows, cols, low, high)

    matrix_3 = add_matrices(matrix_1, matrix_2)

    print_matrix(matrix_1, "Матрица 1")
    print_matrix(matrix_2, "Матрица 2")
    print_matrix(matrix_3, "Сумма (Матрица 3)")
