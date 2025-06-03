# Задача 2: 
number = int(input("Введите пятизначное целое число: "))

# Разряды
units         =  number % 10                 # единицы
tens          = (number // 10)     % 10      # десятки
hundreds      = (number // 100)    % 10      # сотни
thousands     = (number // 1000)   % 10      # тысячи
ten_thousands =  number // 10000            # десятки тысяч

numerator   = (tens ** units) * hundreds
denominator = ten_thousands - thousands
result      = numerator / denominator        

print("Результат:", result)
