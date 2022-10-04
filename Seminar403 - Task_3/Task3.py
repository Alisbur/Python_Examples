num_1=int(input("Введите первое число: "))
num_2=int(input("Введите второе число: "))

res=0
for i in range(2, int(min(num_1,num_2)/2)):
    if num_1%i==0 and num_2%i==0:
        res=i
        break

if res!=0:
    print(f"НОК чисел {num_1} и {num_2} -> {res}")
else:
    print(f"У чисел {num_1} и {num_2} НОК отсутсвует")