"""Задача 3: ax+b=0 (с помощью функции)

Решите уравнение ax + b = 0.

Входные данные
Вводится строка вида ax + b = 0 без пробелов. a, b — произвольные натуральные числа.

Выходные данные
Выведите одно действительное число — корень уравнения.

"""


def uravnenie(a, b):
    if a == 0 and b == 0:
        return "INF"  # Решений бесконечно много
    elif a == 0 and b != 0:
        return "NO"  # Решений нет
    else:
        return -b / a


formula = input()

a = int(formula[:formula.find('x')])
b = int(formula[formula.find('x') + 1:formula.find('=')])

print(uravnenie(a, b))
