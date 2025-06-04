pets = {}

name   = input("Введите кличку питомца: ")
kind   = input("Введите вид питомца: ")
age    = int(input("Введите возраст питомца (целое число): "))
owner  = input("Введите имя владельца: ")

pets[name] = {
    "Вид питомца":    kind,
    "Возраст питомца": age,
    "Имя владельца":  owner
}

def age_suffix(n: int) -> str:
    if 11 <= n % 100 <= 14:      
        return "лет"
    if n % 10 == 1:              
        return "год"
    if 2 <= n % 10 <= 4:        
        return "года"
    return "лет"                

for pet_name in pets.keys():              
    info = pets[pet_name]                 
    years = age_suffix(info["Возраст питомца"])
    print(
        f'Это {info["Вид питомца"]} по кличке "{pet_name}". '
        f'Возраст питомца: {info["Возраст питомца"]} {years}. '
        f'Имя владельца: {info["Имя владельца"]}'
    )
