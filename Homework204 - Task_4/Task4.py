# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import random

n = int(input("Введите число N: "))

mylist = []

for i in range(0, n):
    mylist.append(int(random()*2*n-n))

print(mylist)

result = 1

f = open('Homework204 - Task_4\\Nums.txt')
try:
    for line in f:
        try:
            result *= mylist[int(line.strip())-1]
        except ValueError:
            print("В файле содержится неправильное значение")
            result = 0
finally:
    f.close()

print(result)
