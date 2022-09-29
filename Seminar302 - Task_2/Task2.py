my_list = ["sdf", "gfsdg", 2, "asd", "gfsdg", 0, "sdf"]

print(my_list)

sub_string = input("Введите строку: ")

num = 0

for i in range(0, len(my_list)):
    if sub_string == my_list[i]:
        num += 1
        if num == 2:
            print(f"Позиция второго вхождения {i}")

if num < 2:
    print("-1")
