# class_amount = 3 int(input("Сколько математических классов вам надо?\n"))
# classes = int[]
import math
class_amount1 = int(input("Введите количество учеников в 1 классе\n"))
class_amount2 = int(input("Введите количество учеников в 2 классе\n"))
class_amount3 = int(input("Введите количество учеников в 3 классе\n"))
result = (class_amount1//2) + (class_amount1%2)+(class_amount2//2) + (class_amount2%2)+(class_amount3//2) + (class_amount3%2)
print(result)