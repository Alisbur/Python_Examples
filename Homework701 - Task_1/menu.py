import os

def menu():

    operation = 0

    print()
    print("ПРОГРАММА - ТЕЛЕФОННЫЙ СПРАВОЧНИК\n")
    print("1. Вывести данные из файла db.csv")
    print("2. Вывести данные из файла db.json")
    print("3. Вывести данные из файла db.xml")
    print("4. Добавить новый контакт")    
    print("5. Удалить контакт\n")    
    print("6. Сохранить данные в db.csv")
    print("7. Сохранить данные в db.json")
    print("8. Сохранить данные в db.xml\n")
    print("0. Выход\n")

    while True:
        try:
            point = int(input("Введите номер пункта меню: "))
            if point in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
                break
        except ValueError:
            print("Введён неправильный пункт меню. Попробуйте ещё раз.")

    if point in [1, 2, 3, 4, 5, 6, 7, 8]:
        operation = point
    else:
        exit()

    return operation