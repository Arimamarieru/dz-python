m = int(input("Максимальная грузоподъёмность лодки (m): "))
n = int(input("Количество рыбаков (n): "))

print(f"Введите вес {n} рыбаков, каждый с новой строки:")
weights = [int(input(f"Вес {i + 1}-го рыбака: ")) for i in range(n)]

weights.sort()                

i, j = 0, n - 1              
boats = 0

while i <= j:
    if weights[i] + weights[j] <= m:   
        i += 1                         
    j -= 1                             
    boats += 1                         

print("Минимальное количество лодок:")
print(boats)
