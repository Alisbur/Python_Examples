# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import random

N=int(input("Введите число N: "))

myList = []

for i in range(0,N):
    myList.append(int(random()*2*N-N))

print(myList)

result=1

f=open('Homework204 - Task_4\\Nums.txt')
try:
    for line in f:
        try:
            result*=myList[int(line.strip())-1]
        except ValueError:
            print("В файле содержится неправильное значение")
            result=0
finally:
    f.close()

print(result)