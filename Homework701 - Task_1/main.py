from ast import Pass
import os
import datetime
import json
import menu
import IO_csv
import IO_json
import IO_xml
import db_print
import add_contact
import class_person

DB_CSV_PATH = "Homework701 - Task_1\\db.csv"
DB_JSON_PATH = "Homework701 - Task_1\\db.json"
DB_XML_PATH = "Homework701 - Task_1\\db.xml"

data_list = []

db_print.clear()

while True:
    match menu.menu():
        case 1:
            data_list = IO_csv.read_from_csv(DB_CSV_PATH)
        case 2:
            data_list = IO_json.read_from_json(DB_JSON_PATH)
        case 3:
            data_list = IO_xml.read_from_xml(DB_XML_PATH)
        case 4:
            data_list.append(add_contact.add_new_person())
        case 5:
            num = int(input("Введите номер записи, которую следует удалить, 0 для отмены: "))
            if num!=0:
                if num in range(1,len(data_list)+1):
                    data_list.pop(num-1)
                else:
                    print("Введен неправильный номер записи")
        case 6:
            IO_csv.append_to_csv(DB_CSV_PATH, data_list)
        case 7:
            IO_json.append_to_json(DB_JSON_PATH, data_list)
        case 8:
            IO_xml.append_to_xml(DB_XML_PATH, data_list)

    db_print.db_print(data_list)


