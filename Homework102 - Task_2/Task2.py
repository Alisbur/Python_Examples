# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

list=[True,False]

for x in list:
    for y in list:
        for z in list:
            print(f" При x = {x}, y = {y}, z = {z}:  ¬(X ⋁ Y ⋁ Z) -> {not(x or y or z)} | ¬X ⋀ ¬Y ⋀ ¬Z -> {not x and not y and not z}")