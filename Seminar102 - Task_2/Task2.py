# Напишите программу, которая на вход принимает 5 чисел (можно
# списком) и находит максимальное из них.
# Примеры:
# 1 1, 4, 8, 7, 5 -> 8
# 2 78, 55, 36, 90, 2 -> 90

a=[]
ran=range(1,6)

for i in ran:
    a.append(int(input(f"Введите число номер {i}: ")))

max=a[0]
for i in a:
    if max<i:
        max=i

print(f"{a[0]}, {a[1]}, {a[2]}, {a[3]}, {a[4]} -> {max}")
