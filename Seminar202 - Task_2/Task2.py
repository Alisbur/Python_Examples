n = int(input("Введите число n: "))

print("{", end="")

for i in range(1,n+1):
    print(f"{i} : {3*i+1}", end=", ")

print("\b\b}")
