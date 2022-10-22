import os

def menu():

    operation = 0

    print()
    print("ПРОГРАММА - БАЗА ДАННЫХ\n")
    print("1. Загрузить данные из файла db.json\n")

    print("2. Добавить колонку")
    print("3. Удалить колонку\n")

    print("4. Добавить запись")    
    print("5. Изменить запись")
    print("6. Удалить запись\n")

    print("7. Отсортировать по индексам")    
    print("8. Отсортировать по значениям в колонке\n")

    print("9. Сохранить данные в db.json\n")

    print("0. Выход\n")

    while True:
        try:
            point = int(input("Введите номер пункта меню: "))
            if point in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
                break
        except ValueError:
            print("Введён неправильный номер пункта меню. Попробуйте ещё раз.")

    if point in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        operation = point
    else:
        exit()

    return operation