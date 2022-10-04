# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число N: "))
result = []


def Is_Prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if Is_Prime(number):
    result = [1, number]
else:
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            if Is_Prime(i):
                result.append(i)
    result.append(number)

print(f"{number} -> {result}")
