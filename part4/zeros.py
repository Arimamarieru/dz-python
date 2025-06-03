n = int(input("Сколько чисел вы собираетесь ввести? "))
zeros = 0

for i in range(1, n + 1):
    if int(input(f"Введите число №{i}: ")) == 0:
        zeros += 1

print("Количество нулей:", zeros)
