""" Количество различных элементов списка

Напишите программу, которая подсчитывает, сколько различных чисел содержится в данном
списке.

Входные данные
Программа получает на вход несколько чисел (не более 1000), записанных в одной строке
Все числа по модулю не провосходят 10**9

Выходные данные
Программа должна вывести единственное число - количество различных чисел среди
данных.

"""

sp = list(map(int,input().split()))
spCount = []

for element in sp:
    if element not in spCount:
        spCount.append(element)

print(len(spCount))