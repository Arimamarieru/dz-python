seq = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

seen = set()
print("Ответ:")
for x in seq:
    if x in seen:
        print("YES")
    else:
        print("NO")
        seen.add(x)
