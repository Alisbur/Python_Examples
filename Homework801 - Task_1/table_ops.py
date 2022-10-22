import time

def add_col(db_dict, col):
    if db_dict:
        for key in db_dict.keys():
            db_dict[key][col] = None
    else:
        db_dict[1] = {col : None}
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


def add_row(db_dict, key, new_row):
    if key in db_dict.keys():
        print(f"\nВ таблице уже имеется строка с индексом {key}. Ничего не изменилось.\n")
    else:
        db_dict[key] = new_row
        print(f"\nВ таблицу добавлена строка с индексом {key}.\n")
    time.sleep(1)
    return db_dict


def mod_row(db_dict, key):
    while True:
        new_key = input(f"Индекс строки {key}. Введите новый индекс или нажмите Ввод.\n")
        if new_key != "":
            if int(new_key) not in list(db_dict.keys()):
                break
            else:
                print(f"\nВведённый ключ уже используется в таблице. Используйте другой.\n")
        else:
            new_key=key
            break
    if new_key != key:
        db_dict[int(new_key)] = db_dict[int(key)]

    for el in db_dict[int(key)].keys():
        new_val = input(f"Значение {el} равно {db_dict[int(key)][el]}. Введите новое значение или нажмите Ввод.\n")
        if new_val != "":
            db_dict[int(new_key)][el] = new_val
    if new_key != key:
        db_dict.pop(int(key))
    print(f"\nИзменения внесены в запись.\n")
    time.sleep(1)
    return db_dict


def del_row(db_dict, key):
    if int(key) in list(db_dict.keys()):
        db_dict.pop(int(key))
        print(f"\nСтрока с индексом {key} удалена.\n")
    else:
        print(f"\nВ таблице отсутствует строка с индексом {key}. Удаление невозможно.\n")
    time.sleep(1)
    return db_dict


def sort_table_key(db_dict):
    if db_dict:
        sorted_tuple = sorted(db_dict.items(), key=lambda x: x[0])
        print("Строки отсортированы по индексам.")
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
            sorted_tuple = sorted(db_dict.items(), key=lambda x: x[1][col_name], reverse = reverse_sort)
            print(f"\nТаблица отсортирована по {'возрастанию' if not reverse_sort else 'убыванию'} значений в столбце {col_name}.\n")
            time.sleep(1)       
            return dict(sorted_tuple)
        else:
            print("В таблице нет указанной колонки. Данные не были отсортированы.")                
    print("В таблице нет данных для сортировки")    
    time.sleep(1)     
    return db_dict

    