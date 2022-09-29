# Реализуйте алгоритм перемешивания списка.

from random import random

def ListShuffle(listToShuffle, shuffleTimes):
    for i in range(0,shuffleTimes): 
        index1=0
        index2=0
        while index1==index2:
            index1 = int(random()*(len(listToShuffle)-1))
            index2 = int(random()*(len(listToShuffle)-1))
        temp=listToShuffle[index1]
        listToShuffle[index1]=listToShuffle[index2]
        listToShuffle[index2]=temp
    return listToShuffle

listLen=int(input("Введите длину массива N: "))
myList = []
for i in range(0,listLen):
    myList.append(int(random()*listLen*2-listLen))
print(myList)

shuffleTimes=int(input("Введите количество перемешиваний списка: "))
print(ListShuffle(myList,shuffleTimes))



