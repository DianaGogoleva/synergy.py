pets = {}  

pet_name = input("Введите имя питомца: ")  
pet_type = input("Введите вид питомца: ")  
pet_age = int(input("Введите возраст питомца: "))  
owner_name = input("Введите имя владельца: ")  

pets[pet_name] = {'Вид питомца': pet_type, 'Возраст питомца': pet_age, 'Имя владельца': owner_name}  

age_word = "лет"
if pet_age % 10 == 1 and pet_age % 100 != 11:
    age_word = "год" 
elif pet_age % 10 in [2, 3, 4] and pet_age % 100 not in [12, 13, 14]:
    age_word = "года"

pet_info = pets[pet_name]

print(f'Это {pet_info["Вид питомца"]} по кличке "{pet_name}". '
f'Возраст питомца: {pet_info["Возраст питомца"]} {age_word}. '
f'Имя владельца: {pet_info["Имя владельца"]}')