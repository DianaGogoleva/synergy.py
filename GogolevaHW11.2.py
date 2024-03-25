import collections

pets = {
    1: {"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
    2: {"Каа": {"Вид питомца": "желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"}}
}

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    if 10 < age < 15 or age % 10 == 0 or 5 <= age % 10 <= 9:
        return "лет"
    elif age % 10 == 1:
        return "год"
    else:
        return "года"

def create():
    last = collections.deque(pets, maxlen=1)[0]
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = input("Введите возраст питомца: ")
    owner_name = input("Введите имя владельца: ")
    pets[last + 1] = {pet_name: {"Вид питомца": pet_type, "Возраст питомца": pet_age, "Имя владельца": owner_name}}
    
def read(ID):
    pet_info = get_pet(ID)
    if pet_info:
        for pet_name, info in pet_info.items():
            print(f'Это {info["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {info["Возраст питомца"]} {get_suffix(int(info["Возраст питомца"]))}. Имя владельца: {info["Имя владельца"]}')
            
def update(ID):
    pet_info = get_pet(ID)
    if pet_info:
        update_what = input("Что вы хотите обновить? Вид питомца - введите 1, Возраст питомца - введите 2, Имя владельца - введите 3: ")
        if update_what in ["1", "2", "3"]:
            update_to = input("Введите новое значение: ")
            for pet_name, info in pet_info.items():
                if update_what == "1":
                    info["Вид питомца"] = update_to
                elif update_what == "2":
                    info["Возраст питомца"] = update_to
                elif update_what == "3":
                    info["Имя владельца"] = update_to
                    
def delete(ID):
    if get_pet(ID):
        del pets[ID]
                    
def pets_list():
    for ID, pet_info in pets.items():
        for pet_name, info in pet_info.items():
            print(f'ID: {ID}. Это {info["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {info["Возраст питомца"]} {get_suffix(int(info["Возраст питомца"]))}. Имя владельца: {info["Имя владельца"]}')

command = ""
while command != 'stop':
    command = input("Введите команду (create, read, update, delete, list, stop): ")
    if command == 'create':
        create()
    elif command == 'read':
        ID = int(input("Введите ID питомца: "))
        read(ID)
    elif command == 'update':
        ID = int(input("Введите ID питомца: "))
        update(ID)
    elif command == 'delete':
        ID = int(input("Введите ID питомца: "))
        delete(ID)
    elif command == 'list':
        pets_list()