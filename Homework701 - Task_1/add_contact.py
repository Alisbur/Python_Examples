import class_person

def add_new_person():
    new_person = class_person.person_contact(input("Введите фамилию: "), input("Введите имя: "), input("Введите телефон: "), input("Введите комментарий: "))
    return new_person