print("Введите два целых числа A и B:")
a, b = map(int, input().split())

start = a if a % 2 == 0 else a + 1
even_numbers = list(range(start, b + 1, 2))

print(f"Чётные числа на отрезке от {a} до {b}:")
print(*even_numbers)
