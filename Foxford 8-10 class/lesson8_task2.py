""" Наименьший положительный элемент списка
Напишите программу, которая находит в данном списке наименьший положительный
элемент.

Входные данные
Программа получает на вход несколько чисел (не более 100000), записанных в одной строке
через пробел. Все числа по модулю не превосходят 10 9 . Среди чисел есть хотя бы одно
положительное.

Выходные данные
Программа должна вывести единственное число - наименьшее положительное число среди
данных.

"""

sp = list(map(int,input().split()))
print(sp)
mini = 10**9+1 # sp[0] или присваеваем 1 элемент списка
for element in sp:
    if element > 0 and element < mini:
        mini = element

print(mini)