"""Задача 3: ax+b=0

Решите уравнение ax + b = 0.

Входные данные
Вводится строка вида ax + b = 0 без пробелов. a, b — произвольные натуральные числа.

Выходные данные
Выведите одно действительное число — корень уравнения.

"""

formula = input()

a = int(formula[:formula.find('x')])
b = int(formula[formula.find('x')+1:formula.find('=')])

if a == 0 and b == 0:
    print("INF") #Решений бесконечно много
elif a == 0 and b != 0:
    print("NO") #Решений нет
else:
    x = -b / a
    print(x)
