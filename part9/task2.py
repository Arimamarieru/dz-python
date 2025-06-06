import collections

def get_suffix(age: int) -> str:
    
    if 11 <= age % 100 <= 14:  
        return 'лет'
    if age % 10 == 1:          
        return 'год'
    if 2 <= age % 10 <= 4:     
        return 'года'
    return 'лет'               

def get_pet(pet_id: int):
    
    return pets.get(pet_id, False)

def pets_list() -> None:
    
    if not pets:
        print('База пуста.')
        return
    for pid, record in pets.items():
        name, info = next(iter(record.items()))
        print(f'ID {pid}: {info["Вид питомца"]} "{name}", '
              f'{info["Возраст питомца"]} {get_suffix(info["Возраст питомца"])} '
              f'(владелец: {info["Имя владельца"]})')


def create() -> None:

    last_id = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last_id + 1

    name  = input('Кличка: ')
    kind  = input('Вид: ')
    age   = int(input('Возраст: '))
    owner = input('Имя владельца: ')

    pets[new_id] = {
        name: {
            'Вид питомца':    kind,
            'Возраст питомца': age,
            'Имя владельца':  owner
        }
    }
    print(f'Питомец добавлен с ID {new_id}.')

def read() -> None:
  
    pid = int(input('Введите ID питомца: '))
    rec = get_pet(pid)
    if not rec:
        print('Такого питомца нет.')
        return
    name, info = next(iter(rec.items()))
    print(f'Это {info["Вид питомца"]} по кличке "{name}". '
          f'Возраст питомца: {info["Возраст питомца"]} '
          f'{get_suffix(info["Возраст питомца"])}. '
          f'Имя владельца: {info["Имя владельца"]}')

def update() -> None:
 
    pid = int(input('Введите ID питомца для обновления: '))
    rec = get_pet(pid)
    if not rec:
        print('Такого питомца нет.')
        return

    name, info = next(iter(rec.items()))
    print('Оставьте поле пустым, если менять его не нужно.')

    new_name  = input(f'Кличка [{name}]: ') or name
    new_kind  = input(f'Вид [{info["Вид питомца"]}]: ') or info["Вид питомца"]
    age_in    = input(f'Возраст [{info["Возраст питомца"]}]: ')
    new_age   = int(age_in) if age_in else info["Возраст питомца"]
    new_owner = input(f'Владелец [{info["Имя владельца"]}]: ') or info["Имя владельца"]

    pets[pid] = {
        new_name: {
            'Вид питомца':    new_kind,
            'Возраст питомца': new_age,
            'Имя владельца':  new_owner
        }
    }
    print('Данные обновлены.')

def delete() -> None:
 
    pid = int(input('Введите ID питомца для удаления: '))
    if pets.pop(pid, None):
        print('Запись удалена.')
    else:
        print('Такого питомца нет.')

COMMANDS = {
    'create': create,
    'read':   read,
    'update': update,
    'delete': delete,
    'list':   pets_list,
}

if __name__ == '__main__':
    print('Доступные команды: create, read, update, delete, list, stop')
    while True:
        command = input('> ').strip().lower()
        if command == 'stop':
            break
        action = COMMANDS.get(command)
        if action:
            action()
        else:
            print('Неизвестная команда.')
