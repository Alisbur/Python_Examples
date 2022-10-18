# ДЗ СЕМИНАРА 2

# ЗАДАЧА 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

result = 0
number = input("Введите вещественное число: ")
for el in map(int, [ch for ch in number if ch.isdigit()]):
    result += el    
print(result)


# ЗАДАЧА 2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

result = [1]
n = int(input("Введите число N: "))
for el in [x for x in range (2,n+1)]:
    result.append(result[-1]*el) 
print(result)



# ЗАДАЧА 3
# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

result = 0
n = int(input("Введите число N: "))
for el in map(lambda x: (1+1/x)**x, [k for k in range(1,n+1)]):
    result += el 
print(result)


# ЗАДАЧА 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

result = 1
n = int(input("Введите число N: "))
with open("file.txt", "r") as data:
    for pos in [int(line.strip()) for line in data]:
        result *= [x for x in range(-n, n+1)][int(pos)]
print(result)

