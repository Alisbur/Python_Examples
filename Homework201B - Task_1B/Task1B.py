# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

temp = number = round(float(input("Введите вещественное число: ")), 5)
sum = 0
count = 0

while number//10**count > 0:
    count += 1

while number > 0 and count > -5:  # - Точность до 5 знака после запятой или рассчёт становится бесконечным из-за погрешности
    count -= 1
    digit = int(number/10**count)
    number -= digit*10**count
    sum += digit

print(f"Сумма всех цифр в числе {round(temp,5)} -> {sum}")
