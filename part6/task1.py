N = int(input("Введите количество элементов массива N: "))
nums = []

print(f"Введите {N} целых чисел, каждое с новой строки:")
for i in range(1, N + 1):
    nums.append(int(input(f"{i}-е число: ")))

print("Перевернутый массив:")
print(*nums[::-1])
