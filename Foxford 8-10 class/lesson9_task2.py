"""Самое частое число

Напишите программу, которая находит в данном списке A число, которое встречается в списке наибольшее число раз.

Входные данные
Программа получает на вход несколько чисел (не более 1000), записанных в одной строке через пробел. Все числа по модулю не превосходят 10**9 .

Выходные данные
Программа должна вывести единственное число - число, которое встречается чаще всех из данных. Если таких чисел несколько, то нужно вывести наибольшее из них.

"""
# Первый вариант
#A = [3, 5, 5, 1, 21, 5, 21, 21, ]  # A = list(map(int, input().split()))
#c = 0
#a = 0
#for i in A:
    #if A.count(i) >= c:
        #if i > a:
            #c = A.count(i)
            #a = i
#print(a)

# Второй вариант

def SelectionSort(A):
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]

A = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 7, 1000]
SelectionSort(A)
# print(A)

element = A[0]
number = 0
counts = 1
counts_max = 0

for i in range(1, len(A)):
    if element == A[i]:
        counts += 1
        if counts >= counts_max:
            counts_max = counts
            number = A[i]
    else:
        counts = 1
        element = A[i]

print(number)