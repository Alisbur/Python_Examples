str1=input("Введите первую строку: ")
str2=input("Введите вторую строку: ")

if len(str1)>len(str2):
    target=str2
    source=str1
else:
    target=str1
    source=str2

flag=False
count=0

for i in range(0,len(source)):
    if len(source)-i<len(target):
        break
    elif source[i]==target[0]:
        for j in range (0,len(target)):
            if source[i+j]==target[j]:
                flag=True
            else:
                flag=False
                break
    if flag==True:
        count+=1
        i=i+len(target)
    flag=False

print(count)