# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
listn = list()
n = int(input('Введите количество элементов в массиве:  '))
for i in range(0,n):
    
    listn.append(random.randint(0,10))
print(listn)
x = int(input('Введите число X:  '))
if listn.count(x) > 0:
    print(x)
else:
    min=listn[0]
    for j in range(0,len(listn)):
        if (abs(min-x))>=(abs(listn[j]-x)):
            min=listn[j]
    print(min)
