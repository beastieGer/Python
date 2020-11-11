""" ===��������===
N-���������
n! = 1, ���� n=1
n! = (n-1)! * n, �����
"""


def f(x):
    if(x == 1):
        return x
    return f(x - 1) * x


print(f(5))


"""����� ��������
0 1 2 3 4 5 6  7  8  ...
1 1 2 3 5 8 13 21 34 ...
f(n) = 1, ���� n = 0, 1
f(n) = (n-1) + (n-2)
"""
#������������������ ������, ��������� ������ ��� ��������� �����
#����� ��� ������� ���������� ���� ����� �������� ��������, ����� �� ������� � ������ ���-�� ����� ��������


def fib(x):
    if(x == 1 or x == 0):
        return 1
    return fib(x - 1) + fib(x - 2)


# ������������ ����������������
# �������� ������������� � ����, �����)


def fib_dinamic(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return b


# print(fib(28))
print(fib_dinamic(100))


"""
��������� �����
"""


def Hanoi(n, start, finish, help):
    if n > 0:
        Hanoi(n - 1, start, help, finish)
        print(start, '->', finish)
        Hanoi(n - 1, help, finish, start)


Hanoi(3, 1, 3, 2)


"""
������ ��������� ����������
"""

s = '1+2+3*4+2*4*6*2+2*3+1'


def calc(s):
    if '+' in s:
        place = s.rfind('+')
        return calc(s[:place]) + calc(s[place + 1:])
    elif '*' in s:
        place = s.rfind('*')
        return calc(s[:place]) * calc(s[place + 1:])
    else:
        return int(s)


print(calc(s))

"""
��������
"""

from turtle import *

def fractal(n):
   if n > 0:
      fractal(n - 1)
      left(60)
      fractal(n - 1)
      right(120)
      fractal(n - 1)
      left(60)
      fractal(n-1)
   else:
      forward(3)

fractal(5)
input()