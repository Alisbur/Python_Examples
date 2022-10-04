# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import random

num_list = []

list_len = int(input("Введите длину списка N: "))
for i in range(0, list_len):
    num_list.append(round(random()*10, 2))

max_fract = min_fract = num_list[0]-int(num_list[0])

for i in num_list:
    if max_fract < i-int(i):
        max_fract = i-int(i)
    if min_fract > i-int(i):
        min_fract = i-int(i)

print(f"{num_list} => {round(max_fract-min_fract,2)}")


# lst = [1.1, 1.2, 3.1, 5, 10.01]

# lst = [round(val % 1, 2) for val in lst]
# rev_result = max(lst) - min(lst)