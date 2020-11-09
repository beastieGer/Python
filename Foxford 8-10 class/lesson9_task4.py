"""Случайное перемешивание

Может ли при случайном перемешивании массива 1, 2, 3, 4, 5 при помощи метода
random.shuffle() получиться массив 1, 2, 3, 4, 5?

"""

import random

lst = [1, 2, 3, 4, 5]

tmp_lst = lst[:]
cnt = 1
random.shuffle(tmp_lst)
while lst != tmp_lst:
    cnt += 1
    print(tmp_lst)
    random.shuffle(tmp_lst)
print(tmp_lst)
print('EQUAL: count =', cnt)

#Да, может, и это правильно: тождественная перестановка тоже является перестановкой и может получиться случайно.