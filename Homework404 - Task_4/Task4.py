# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import random

k = int(input("Введите степень многочлена k: "))
s = ""
coefficients = []

for i in range(0, k+1):
    coefficients.append(int(random()*200-100))

print(f"k = {k} => ", end="")

for i, el in enumerate(coefficients):
    if el < 0:
        s += f"- {-el}"
    if el > 0:
        if i == 0:
            s += f"{el}"
        else:
            s += f"+ {el}"
    if el != 0:
        if i == len(coefficients)-2:
            s += "x "
        elif i != len(coefficients)-1:
            s += f"x^{len(coefficients)-i-1} "
s += " = 0"

with open('Homework404 - Task_4\\Nums.txt', 'w') as data:
    data.write(s)
