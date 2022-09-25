# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

list=[True,False]
# y=[True,False]
# z=[True,False]

for x in list:
    for y in list:
        for z in list:
            # res1 = not(x or y or z)
            # res2 = not x and not y and not z
            print(f" При x = {x}, y = {y}, z = {z}:  ¬(X ⋁ Y ⋁ Z) -> {not(x or y or z)} | ¬X ⋀ ¬Y ⋀ ¬Z -> {not x and not y and not z}")