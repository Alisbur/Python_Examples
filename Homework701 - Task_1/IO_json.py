import class_person
import json

def read_from_json(db_path):
    result = []
    with open(db_path, "r", encoding="UTF-8") as source:
        top_list = json.load(source)
    for el in top_list:
        result.append(class_person.person_contact(el[0], el[1], el[2], el[3]))
    return result


def append_to_json(db_path, data_list):
    top_list=[]
    el_list=[]
    with open(db_path, 'w', encoding="UTF-8") as source:
        for el in data_list:
            el_list=[]
            el_list.append(el.l_name)
            el_list.append(el.f_name)
            el_list.append(el.phone_number)
            el_list.append(el.comment)
            top_list.append(el_list)
        json.dump(top_list, source, indent = 4)
    return 0