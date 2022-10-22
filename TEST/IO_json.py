import json

def read_from_json(db_path):
    with open(db_path, "r", encoding="UTF-8") as source:
        db_list = json.load(source)
    return db_list

def append_to_json(db_path, db_list):
    with open(db_path, 'w', encoding="UTF-8") as source:
        json.dump(db_list, source, indent = 4)
    return 0