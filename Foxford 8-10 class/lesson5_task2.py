"""Сумма кубов

Вычислите при помощи языка Питон сумму кубов натуральных чисел от 1 до 100:
1**3+2**3+3**3+...+100**3

"""

sumCube = 0

for i in range(1, 101):
    sumCube += i ** 3

print(sumCube)
