# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# f(-n)=F(n)*(-1)^n+1

def fib(n):
    if (n < 0):
        if n == -1:
            return 1
        else:
            return int(fib(-n)*(-1)**(n+1))
    else:
        if n == 0 or n == 1:
            return n
        else:
            return fib(n-1)+fib(n-2)

fib_list = []
lim = int(input("Введите предел для вывода чисел Фибоначчи и негафибоначчи: "))

for i in range(-lim, lim+1):
    fib_list.append(fib(i))

print(fib_list)
