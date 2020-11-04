"""ax+b=0 -- 2 (с помощью функции)

Решите уравнение ax + b = 0.

Входные данные
Вводится строка в формате
ax + b = 0
или
ax - b = 0
где вместо a — целое число, вместо b — целое неотрицательное число. Числа по модулю не
превосходят 1000. Число a может быть пропущено, если оно равно 1. b всегда присутствует,
x также всегда присутствует, даже если а = 0

Выходные данные
Выведите корни уравнения, если их конечное число; 'NO', если корней нет и 'INF', если
корней бесконечно много.

"""


def uravnenie(b):
    if 'x' == formula[0]:
        a = 1
    else:
        a = int(formula[:formula.find('x')])

    if '0' == formula[0] and b == 0:
        return 'INF'
    elif '0' == formula[0]:
        return 'NO'
    else:
        return -1 * b / a


formula = input()

b = int(formula[formula.find('x') + 1:formula.find('=')])

print(uravnenie(b))