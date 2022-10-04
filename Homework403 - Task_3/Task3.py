# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import random

result = []

list_Len = int(input("Введите длину массива N: "))
my_list = []
for i in range(0, list_Len):
    my_list.append(int(random()*list_Len*2-list_Len))

print(my_list, end=" -> ")

while len(my_list) > 0:
    unique = True
    val = my_list.pop()
    while val in my_list:
        my_list.remove(val)
        unique = False
    if unique:
        result.append(val)

print(result)
