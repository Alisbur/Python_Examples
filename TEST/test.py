import IO_json
DB_JSON_PATH = "TEST\\db.json"

def add_col(db_dict, col):
    for key in db_dict.keys():
        db_dict[key][col] = None
    return db_dict

def del_col(db_dict, col):
    for key in db_dict.keys():
        db_dict[key].pop(col)
    return db_dict

def add_row(db_dict, key, new_row):
    if key in db_dict.keys():
        return db_dict
    else:
        db_dict[key] = new_row
        return db_dict

def del_row(db_dict, key):
    if key in db_dict.keys():
        db_dict.pop(key)
        return db_dict
    else:
        return db_dict

db_dict = {}
db_dict = add_row(db_dict, 0, {"Name":"George","Age":14, "Status":"Sudent"})
db_dict = add_row(db_dict, 1, {"Name":"Michael","Age":10, "Status":"Student"})
db_dict = add_row(db_dict, 2, {"Name":"Nikolay","Age":3, "Status":"Child"})

print("\nИсходный текст")

for key in db_dict.keys():
    print(f"{key} - {db_dict[key]}")

db_dict = add_col(db_dict, "Group")

print("\nДобавили колонку Gropu")

# for key in db_dict.keys():
#     print(f"{key} - {db_dict[key]}")

# db_dict = del_col(db_dict, "Age")

# print("\nУдалили колонку Age")

# for key in db_dict.keys():
#     print(f"{key} - {db_dict[key]}")

# db_dict = del_row(db_dict, 1)

# print("\nУдалили строку 1")

# for key in db_dict.keys():
#     print(f"{key} - {db_dict[key]}")
    
IO_json.append_to_json(DB_JSON_PATH, db_dict)

# db_dict = IO_json.read_from_json(DB_JSON_PATH)

# print("\nЗаписали в файл и прочли оттуда")

# for key in db_dict.keys():
#     print(f"{key} -> {db_dict[key]}")




# def add_col(db_list, col):
#     for el in db_list:
#         el[col] = None
#     return db_list

# def del_col(db_list, col):
#     for el in db_list:
#         el.pop(col)
#     return db_list


# db_list = []
# db_list.append({"Name":"George","Age":14, "Status":"Sudent"})
# db_list.append({"Name":"Michael","Age":10, "Status":"Student"})
# db_list.append({"Name":"Nikolay","Age":3, "Status":"Child"})

# for ind, el in enumerate(add_col(db_list, "Group")):
#     print(f"{ind} - {el}")

# for ind, el in enumerate(del_col(db_list, "Age")):
#     print(f"{ind} - {el}")

# IO_json.append_to_json(DB_JSON_PATH, db_list)

# print()

# for ind, el in enumerate(IO_json.read_from_json(DB_JSON_PATH)):
#     print(f"{ind} - {el}")




