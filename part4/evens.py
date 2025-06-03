print("Введите два целых числа A и B:")
a, b = map(int, input().split())

start = a if a % 2 == 0 else a + 1
print(*range(start, b + 1, 2))
