from ast import Pass
import os
import datetime
import json
import menu
import IO_json
import db_print
import table_ops

DB_JSON_PATH = "Homework801 - Task_1\\db.json"

db_dict = {}

db_print.clear()

while True:
    match menu.menu():
        case 1:
            db_dict = IO_json.read_from_json(DB_JSON_PATH)

        case 2:
            col_name = input(
                "Введите название новой колонки или 0 для отмены: ")
            if col_name != "0":
                db_dict = table_ops.add_col(db_dict, col_name)
        case 3:
            col_name = input(
                "Введите название колонки, которую следует удалить или 0 для отмены: ")
            if col_name != "0":
                db_dict = table_ops.del_col(db_dict, col_name)

        case 4:
            db_dict = table_ops.add_row(db_dict)
        case 5:
            while True:
                row_to_modify = input(
                    "Введите ключ записи, которую следует изменить, 0 для отмены: ")
                if row_to_modify.isdigit():
                    break
                else:
                    print("Ошибка ввода! Номер должен быть числом.\n")
            if row_to_modify != "0":
                db_dict = table_ops.mod_row(db_dict, int(row_to_modify))
        case 6:
            while True:
                row_to_del = input(
                    "Введите ключ записи, которую следует удалить, 0 для отмены: ")
                if row_to_del.isdigit():
                    break
                else:
                    print("Ошибка ввода! Номер должен быть числом.\n")
            if row_to_del != "0":
                db_dict = table_ops.del_row(db_dict, int(row_to_del))

        case 7:
            db_dict = table_ops.sort_table_key(db_dict)
        case 8:
            col_name = input(
                "Введите название колонки по которой будет произведена сортировка или 0 для отмены: ")
            if col_name != "0":
                db_dict = table_ops.sort_table_val(db_dict, col_name)

        case 9:
            IO_json.append_to_json(DB_JSON_PATH, db_dict)

    db_print.db_print(db_dict)
