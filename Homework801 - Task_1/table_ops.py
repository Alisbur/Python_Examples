import time


def add_col(db_dict, col):
    if db_dict:
        for key in db_dict.keys():
            db_dict[key][col] = None
    else:
        db_dict[1] = {col: None}
    print(f"\nВ таблицу добавлена колонка {col}.\n")
    time.sleep(1)
    return db_dict


def del_col(db_dict, col):
    was_deleted = False
    for key in db_dict.keys():
        if col in db_dict[key].keys():
            db_dict[key].pop(col)
            was_deleted = True
    if not was_deleted:
        print(f"\nВ таблице отсутствует колонка {col}. Удаление невозможно.\n")
    else:
        print(f"\nКолонка {col} удалена.\n")
    time.sleep(1)
    return db_dict


def add_row(db_dict):
    new_row_dict = {}
    if db_dict:
        new_row_key = max(db_dict.keys())+1

        for key in db_dict[next(iter(db_dict))].keys():
            new_value = input(
                f"Введите значение поля {key} или 0 для отмены: ")
            if new_value == "0":
                break
            new_row_dict[key] = new_value

        if new_value != "0":
            db_dict[new_row_key] = new_row_dict
            print(f"\nВ таблицу добавлена строка с ключом {key}.\n")
    else:
        print("Прежде чем создавать записи создайте хотя бы одну колонку.")
    time.sleep(1)
    return db_dict


def mod_row(db_dict, key):
    while True:
        new_key_str = input(
            f"Ключ строки {key}. Введите новый ключ или нажмите Ввод.\n")
        if not new_key_str.isdigit() and new_key_str != "":
            print(f"\nВведённый ключ не является числом. Используйте другой.\n")
            time.sleep(1)
            continue
        if new_key_str != "":
            new_key = int(new_key_str)
            if new_key not in list(db_dict.keys()):
                break
            else:
                print(
                    f"\nВведённый ключ уже используется в таблице. Используйте другой.\n")
                time.sleep(1)
        else:
            new_key = key
            break

    if new_key != key:
        db_dict[new_key] = db_dict[key]

    for el in db_dict[key].keys():
        new_val = input(
            f"Значение {el} равно {db_dict[key][el]}. Введите новое значение или нажмите Ввод.\n")
        if new_val != "":
            db_dict[new_key][el] = new_val
    if new_key != key:
        db_dict.pop(key)
    print(f"\nИзменения внесены в запись.\n")
    time.sleep(1)
    return db_dict


def del_row(db_dict, key):
    if key in list(db_dict.keys()):
        db_dict.pop(key)
        print(f"\nСтрока с ключом {key} удалена.\n")
    else:
        print(
            f"\nВ таблице отсутствует строка с ключом {key}. Удаление невозможно.\n")
    time.sleep(1)
    return db_dict


def sort_table_key(db_dict):
    if db_dict:
        sorted_tuple = sorted(db_dict.items(), key=lambda x: x[0])
        print("Строки отсортированы по индексам ключей.")
        time.sleep(1)
        return dict(sorted_tuple)
    print("В таблице нет данных для сортировки")
    time.sleep(1)
    return db_dict


def sort_table_val(db_dict, col_name):
    if db_dict:
        reverse_sort = False
        if input("Для сортировки по возрастанию нажмите Ввод. Для сортировки по убыванию введите любое значение: "):
            reverse_sort = True
        if col_name in list(db_dict[list(db_dict.keys())[0]].keys()):
            sorted_tuple = sorted(
                db_dict.items(), key=lambda x: x[1][col_name], reverse=reverse_sort)
            print(
                f"\nТаблица отсортирована по {'возрастанию' if not reverse_sort else 'убыванию'} значений в столбце {col_name}.\n")
            time.sleep(1)
            return dict(sorted_tuple)
        else:
            print("В таблице нет указанной колонки. Данные не были отсортированы.")
    print("В таблице нет данных для сортировки")
    time.sleep(1)
    return db_dict
