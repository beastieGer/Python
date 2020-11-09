"""Анализ частоты
Последовательность чисел генерируется следующей функцией.

seed = 71

def get_number():
    global seed
    seed = (3721*seed+2)%(2**16)
    return seed % 100

Найти самое частое число среди первого миллиона генерируемых ей чисел (то есть миллиона результатов вызова функции).
"""

seed = 71


def get_number():
    global seed
    seed = (3721 * seed + 2) % (2**16)
    return seed % 100


def SimpleCountingSort(A):
    scope = max(A) + 1
    C = [0] * scope
    for x in A:
        C[x] += 1
    # самое частое число среди первого миллиона генерируемых
    print(C.index(max(C)))


A = [get_number() for k in range(1000000)]
SimpleCountingSort(A)


# ВТОРОЙ вариант
#from collections import Counter

#seed = 71
# def get_number():
#global seed
#seed = (3721 * seed + 2) % (2**16)
# return seed % 100

#print(*Counter(get_number() for _ in range(1000000)).most_common(1)[0], sep=' -> ')
