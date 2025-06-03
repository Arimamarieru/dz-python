import math

x = int(input("Введите натуральное число X (≤ 2 000 000 000): "))

cnt = 0
i = 1
while i * i <= x:
    if x % i == 0:
        cnt += 1 if i * i == x else 2
    i += 1

print(cnt)
