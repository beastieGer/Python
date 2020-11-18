""" Игра Крестики и нолики

Игрок играет за Х, компьютер за 0

"""

from random import randint
N = 3
a = [['.'] * N for i in range(N)]

for current in ['X', '0'] * 4 + ['X']:
    if current == 'X':
        move = input('Enter your move: ')
        x, y = map(int, move.split())
        while a[x][y] != '.':
            move = input('Клетка занята, попробуйте ещё раз: ')
            x, y = map(int, move.split())
    else:
        x, y = randint(0, 2), randint(0, 2)
        while a[x][y] != '.':
            x, y = randint(0, 2), randint(0, 2)

    a[x][y] = current

    for i in a:
        print(' '.join(i))
    print("------")

    if a[0][0] == a[1][1] == a[2][2] != '.':
        print("ПОБЕДА" + " победил " + current)
        break

    if a[0][2] == a[1][1] == a[2][0] != '.':
        print("ПОБЕДА" + " победил " + current)
        break

    if a[0][0] == a[0][1] == a[0][2] != '.':
        print("ПОБЕДА" + " победил " + current)
        break

    if a[1][0] == a[1][1] == a[1][2] != '.':
        print("ПОБЕДА" + " победил " + current)
        break

    if a[2][0] == a[2][1] == a[2][2] != '.':
        print("ПОБЕДА" + " победил " + current)
        break

    if a[0][0] == a[1][0] == a[2][0] != '.':
        print("ПОБЕДА" + " победил " + current)
        break

    if a[1][0] == a[1][1] == a[1][2] != '.':
        print("ПОБЕДА" + " победил " + current)
        break

    if a[2][0] == a[2][1] == a[2][2] != '.':
        print("ПОБЕДА" + " победил " + current)
        break
