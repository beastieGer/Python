"""Задача 1: Шестнадцатеричное в двоичное (с помощью функции)

Напишите программу, которая переводит число (возможно, отрицательное), записанное в
шестнадцатеричной системе счисления, в двоичную систему.

Входные данные
Входная строка содержит шестнадцатеричную запись целого числа.

Выходные данные
Программа должна вывести запись этого числа в двоичной системе счисления.

"""


def hex_in_bin(N):
    if ("-" in N) and ('0x' not in N):
        N = "-0x" + N[1:]

    if '0x' not in N:
        N = '0x' + N

    if "-" in N:
        N = N[1:]


N = input()

hex_in_bin(N)

if N[0] == '-':
    print('-' + bin(int(N, 16))[3:])
else:
    print(bin(int(N, 16))[2:])
