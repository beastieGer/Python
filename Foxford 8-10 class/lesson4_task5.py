"""Кинотеатр

N мальчиков и M девочек пошли в кинотеатр и купили билеты
на подряд идущие места в одном ряду. 
Определите, как нужно сесть мальчикам и девочкам, 
чтобы рядом с каждым мальчиком сидела хотя бы одна девочка, 
а рядом с каждой девочкой — хотя бы один мальчик.

Входные данные
Вводятся два числа N и M в отдельных строчках. 
Оба числа - натуральные, не превосходящие 100.

Выходные данные
Выведите какую-нибудь строку, в которой будет ровно N символов
B (обозначающих мальчиков) и M символов G (обозначающих девочек),
удовлетворяющую условию задачи.
Пробелы между символами выводить не нужно.
Если рассадить мальчиков и девочек согласно условию задачи
невозможно, выведите строку NO SOLUTION.

"""

N = int(input())  # boy
M = int(input())  # girl

if N > M * 2 or M > N * 2:
    print("NO SOLUTION")
elif N >= M:
    x = N - M
    y = M - x
    while x:
        print("BGB", end="")
        x -= 1
    while y:
        print("BG", end="")
        y -= 1
else:
    x = M - N
    y = N - x
    while x:
        print("GBG", end="")
        x -= 1
    while y:
        print("GB", end="")
        y -= 1
