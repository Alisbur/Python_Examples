import os

def clear(): return os.system('cls')

def db_print(db_dict):
    clear()

    print("\n")

    if db_dict:
        print("\n│ Ключ │",end="")
        for k in db_dict[next(iter(db_dict))].keys():
            print(f" {str(k):12.12} │",end="")
                
        for key in db_dict.keys():
            # print("\n")
            print(f"\n│ {str(key):4.4} │",end="")
            for k in db_dict[key].keys():
                print(f" {str(db_dict[key][k]):12.12} │",end="")

    print("\n")


             
                
    #              {[k]):3.3}  Фамилия    │      Имя     │     Телефон     │           Комментарий          │")
        
    #     for key in db_dict.keys():
    #         for k in db_dict[key].keys():
    #             db_dict[key][k]
    
    
    
    
    # counter=0
    # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nБАЗА ДАННЫХ\n")
    # print(f"┌─────┬──────────────┬──────────────┬─────────────────┬────────────────────────────────┐")
    # print(f"│     │   Фамилия    │      Имя     │     Телефон     │           Комментарий          │")
    
    # for el in data_list:
    #     counter+=1
    #     print(f"├─────┼──────────────┼──────────────┼─────────────────┼────────────────────────────────┤")
    #     print(f"│{str(counter):5.5}│ {el.l_name:12.12} │ {el.f_name:12.12} │ {el.phone_number:15.15} │ {el.comment:30.30} │")
    # print(f"└─────┴──────────────┴──────────────┴─────────────────┴────────────────────────────────┘")       