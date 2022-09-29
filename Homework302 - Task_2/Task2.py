# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import random

list_len = int(input("Введите длину списка N: "))
num_list = []
result = []

for i in range(0, list_len):
    num_list.append(int(random()*10))

if list_len % 2 == 0:
    limit = int(list_len/2-1)
else:
    limit = int(list_len/2)

for i in range(0, limit+1):
    result.append(num_list[i]*num_list[list_len-1-i])

print(f"{num_list} => {result}")
