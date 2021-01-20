""" Правильная скобочная последовательность

Требуется определить, является ли правильной данная последовательность круглых, квадратных и фигурных скобок.

Входные данные

В единственной строке входных данных записано подряд N скобок (1≤N≤105).

Выходные данные

Выведите «YES», если данная последовательность является правильной, и «NO» в противном случае.

"""

stack = []
def isPair(left, right):
    return left + right in ["()","[]","{}"]

for bracket in input():
    if bracket in '([{':
        stack.append(bracket)
    else:
        if len(stack) == 0:
            print("NO")
            exit(0)
        if not isPair(stack.pop(), bracket):
            print("NO")
            exit(0)

if len(stack) == 0:
    print("YES")
else:
    print("NO")
