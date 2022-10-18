import class_person
import os

def clear(): return os.system('cls')

def db_print(data_list):
    clear()
    counter=0
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nБАЗА ДАННЫХ\n")
    print(f"┌─────┬──────────────┬──────────────┬─────────────────┬────────────────────────────────┐")
    print(f"│     │   Фамилия    │      Имя     │     Телефон     │           Комментарий          │")
    
    for el in data_list:
        counter+=1
        print(f"├─────┼──────────────┼──────────────┼─────────────────┼────────────────────────────────┤")
        print(f"│{str(counter):5.5}│ {el.l_name:12.12} │ {el.f_name:12.12} │ {el.phone_number:15.15} │ {el.comment:30.30} │")
    print(f"└─────┴──────────────┴──────────────┴─────────────────┴────────────────────────────────┘")       