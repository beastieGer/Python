""" Обратный отсчет

A = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Создайте список A при помощи генератора списков.
Срезы не использовать. В генераторе использовать переменную k.
В ответе запишите присваивание с пробелами вокруг оператора присваивания и при
необходимости запятой с одним пробелом после каждой запятой.
Например: A = [k for k in range(10)]


"""

A = [k for k in range(20, 0, -1)]

print(A)
