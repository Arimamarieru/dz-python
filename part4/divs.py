x = int(input())
cnt = 0
i = 1
while i * i <= x:
    if x % i == 0:
        cnt += 1 if i * i == x else 2
    i += 1
print(cnt)
