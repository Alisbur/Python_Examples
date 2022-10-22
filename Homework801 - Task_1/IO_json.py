import time
import json


def read_from_json(db_path):
    with open(db_path, "r", encoding="UTF-8") as source:
        if source.read() == "":
            print(f"\nВ файле отсутствуют данные.\n")
            time.sleep(1)
            return
    with open(db_path, "r", encoding="UTF-8") as source:
        db_list = json.load(source)

    temp_dict = {}
    for key in db_list.keys():
        temp_dict[int(key)] = db_list[key]
    return temp_dict


def append_to_json(db_path, db_list):
    with open(db_path, 'w', encoding="UTF-8") as source:
        json.dump(db_list, source, indent = 4)
    print(f"\nДанные сохранены в {db_path}.\n")
    time.sleep(1)
    return