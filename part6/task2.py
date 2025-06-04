arr = list(map(int, input("Введите целые числа через пробел: ").split()))

result = [arr[-1]] + arr[:-1]

print("Изменённый массив:")
print(*result)
