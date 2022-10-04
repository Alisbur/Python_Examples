# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

file_path1 = "Homework405 - Task_5\\Nums1.txt"
file_path2 = "Homework405 - Task_5\\Nums2.txt"

# Функция, которая превращает список частей уравнения в словарь с ключами - степенями X и коэффициентами


def make_dict_of_equal(parts_list):
    parts_dict = {}
    sign = 1
    for el in parts_list:
        if el == "-":
            sign = -1
            continue
        elif el == "+":
            continue
        if "x^" in el:
            parts_dict[int(el.split("x^")[1])] = int(el.split("x^")[0])*sign
        elif "x" in el:
            parts_dict[1] = int(el.split("x")[0])*sign
        else:
            parts_dict[0] = int(el)*sign
        sign = 1
    return parts_dict


# Считываем в строки многочлены из файлов
with open(file_path1, 'r') as f1:
    equal1 = f1.readline()[:-4]
with open(file_path2, 'r') as f2:
    equal2 = f2.readline()[:-4]

# Превращаем строки в списки разбивая их по пробелам и делаем из них словари с помощью функции make_dict_of_equal
dict1 = make_dict_of_equal(equal1.split(" "))
dict2 = make_dict_of_equal(equal2.split(" "))

target = {}
source = {}

# Определяем в каком многочлене степень выше. Он станет целью (target) в которую будут добавляться значения коэффициентов второго многочлена (source)
if max(list(dict1.keys())) > max(list(dict2.keys())):
    target = dict1.copy()
    source = dict2.copy()
else:
    target = dict2.copy()
    source = dict1.copy()

# Суммируем коэффициенты из souce в target
for key in target.keys():
    if key in source.keys():
        target[key] += source[key]

# Превращаем словарь степеней и коэффициентов в список коэффициентов, чтобы далее использовать алгоритм из задачи №4
coefficients = []
for i in range(max(target.keys()), -1, -1):
    if i in target.keys():
        coefficients.append(target[i])
    else:
        coefficients.append(0)

# Алгоритм формирования строки-многочлена из задачи №4
s = ""
for i, el in enumerate(coefficients):
    if el < 0:
        s += f"- {-el}"
    if el > 0:
        if i == 0:
            s += f"{el}"
        else:
            s += f"+ {el}"
    if el != 0:
        if i == len(coefficients)-2:
            s += "x "
        elif i != len(coefficients)-1:
            s += f"x^{len(coefficients)-i-1} "
s += " = 0"

# Записываем результат в файл Result.txt
with open('Homework405 - Task_5\\Result.txt', 'w') as data:
    data.write(s)
