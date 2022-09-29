# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import random

list_len = int(input("Введите длину списка N: "))
num_list = []
for i in range(0, list_len):
    num_list.append(int(random()*10))

print(f"{num_list} -> на нечётных позициях элементы ", end="")

result=0

for i,el in enumerate(num_list):
    if i%2==1:
        result+=el
        print(f" {el}", end=",")

print(f" ответ: {result}")