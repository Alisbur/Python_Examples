from random import random

list_len = int(input("Введите длину списка N: "))
my_list = []
for i in range(0, list_len):
    my_list.append(int(random()*10-5))
print(my_list)

find_num = int(input("Введите число для поиска: "))

flag = -1

# for i in range(0,len(my_list)):
#     if find_num==my_list[i]:
#         flag=i

for i, el in enumerate(my_list):
    if find_num == el:
        flag = i

if flag >= 0:
    print(f"Число {find_num} присутствует в списке на позиции {flag}")
else:
    print(f"Число {find_num} отсутствует в списке")
