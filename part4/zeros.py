n = int(input())
zeros = 0
for _ in range(n):
    if int(input()) == 0:
        zeros += 1
print(zeros)
