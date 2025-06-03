n = int(input("Введите количество чисел N: "))

zeros = 0
for i in range(1, n + 1):
    if int(input(f"Введите число №{i}: ")) == 0:
        zeros += 1

print(zeros)
