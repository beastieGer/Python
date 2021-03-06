""" k-кузнечик

Кузнечик умеет прыгать на расстояние 1, 2, ... , k клеток (то есть длина прыжка кузнечика не превышает k ). Определите, каким числом способов кузнечик может попасть из точки 0 в
точку n .

Входные данные

Программа получает на вход два числа, записанных в одной строке — n и k ( 0≤n≤30 , 1≤k≤10 ).

Выходные данные

Программа должна вывести одно число — искомое количество способов.

"""

def kuz(n, k):
    a = []
    a.append(1)
    for i in range(1, n + 1):
        r = k
        if (i < r):
            r = i
        a.append(0)
        for j in range(1, r + 1):
            a[i] = a[i] + a[i - j]
    return a[n]


n, k = map(int, input().split())
print(kuz(n, k))
