"""Количество различных элементов списка

Напишите программу, которая подсчитывает, сколько различных чисел содержится в данном
списке.

Входные данные
Программа получает на вход несколько чисел (не более 1000), записанных в одной строке
через пробел. Все числа по модулю не превосходят 10 9 .

Выходные данные
Программа должна вывести единственное число - количество различных чисел среди
данных.

"""

A = [2, 5, 1, 10, 3, 1]  # list(map(int, input().split()))
B = []
a = 0
for i in A:
    if i not in B:
        B.append(i)
print(len(B))