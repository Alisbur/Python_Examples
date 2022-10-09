my_list = [1, 5, 2, 5, 8, 2, 5, 7]
result = []
count = 0
result.append(my_list[0])

for i in my_list:
    if i > result[count]:
        result.append(i)
        count += 1

print(result)
