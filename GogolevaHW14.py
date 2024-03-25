my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list_recursively(lst):
    # базовый случай: список пуст
    if not lst:
        print("Конец списка")
        return
    # шаг рекурсии: выводим первый элемент и затем вызываем функцию для остальной части списка
    print(lst[0])
    print_list_recursively(lst[1:])

print_list_recursively(my_list)