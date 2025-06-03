a, b = map(int, input("Введите два целых числа A и B (через пробел, A ≤ B): ").split())

start = a if a % 2 == 0 else a + 1      # первое чётное ≥ A
print(*range(start, b + 1, 2))
