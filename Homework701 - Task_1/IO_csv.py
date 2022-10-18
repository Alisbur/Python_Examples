import class_person

def read_from_csv(db_path):
    temp_list = []
    result = []
    with open(db_path, "r", encoding="UTF-8") as source:
        for line in source:
            temp_list = line.strip().split(",")
            result.append(class_person.person_contact(temp_list[0], temp_list[1], temp_list[2], temp_list[3]))
    return result


def append_to_csv(db_path, data_list):
    with open(db_path, 'w', encoding="UTF-8") as source:
        for el in data_list:
            source.write(f"{el.l_name},{el.f_name},{el.phone_number},{el.comment}\n")        
    return 0