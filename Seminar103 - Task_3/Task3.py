# Напишите программу, которая будет на вход принимать число N и
# выводить числа от -N до N
# Примеры:
# 1 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

a=int(input("Введите число: "))
r=range(-a,a+1)
s=[]
for i in r:
    s.append(str(i))

print(f"{a} -> {', '.join(s)}")