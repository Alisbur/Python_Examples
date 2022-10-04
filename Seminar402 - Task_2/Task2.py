import math
import numpy as np

a = float(input("Введите A: "))
b = float(input("Введите B: "))
c = float(input("Введите C: "))

# if b**2-4*a*c < 0:
#     print("нет корней")
# elif b**2-4*a*c == 0:
#     print(f"один корень -> {-b/(2*a)}")
# else:
#     print(
#         f"корень 1 -> {round((-b-math.sqrt(b**2-4*a*c))/(2*a),2)}, корень 2 -> {round((-b+math.sqrt(b**2-4*a*c))/(2*a),2)}")

p = [a, b, c]

print(f"{np.roots(p)}")
