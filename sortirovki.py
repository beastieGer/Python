"""
сортировка вставками
"""

s = [345, 678, 23, 0, 43, 67, 78, 536, 565468, -34]
N = len(s)
for j in range(1, N):
    for i in range(j, 0, - 1):
        if s[i] < s[i - 1]:
            s[i], s[i - 1] = s[i - 1], s[i]
        else:
            break
print(s)

"""
пузырьковая сортировка
"""

s = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
N = len(s)
for j in range(N - 1):
    for i in range(N - j - 1):
        if s[i] > s[i + 1]:
            s[i], s[i + 1] = s[i + 1], s[i]
print(s)

"""
сортировка выбором минимума
"""


def SelectionSort(A):
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]


"""
сортировка подсчетом
"""

A = [1, 2, 0, 0, 2, -2, 1, 0, 0, -1, -1, 0]
maximum, minimum = max(A), min(A)
B = [0] * (maximum - minimum + 1)
C = []
for element in A:
    B[element] += 1

for i in range(minimum, maximum + 1):
    C += [i] * B[i]

print(A)
print(B)
print(C)

"""
сортировка подсчетом в общем виде (с ключами)
"""
s = [('Ivanov', 1), ('Petrova', 2), ('Sidorov', 1), ('Ivanova', 3)]

count = [0] * 4
for person in s:
    count[person[1]] += 1

t = [None] * len(s)
index = [0] * 4

for i in range(1, 4):
    index[i] = index[i - 1] + count[i - 1]

for person in s:
    t[index[person[1]]] = person
    index[person[1]] += 1

print(t)


"""
сортировка подсчетом
"""

def SimpleCountingSort(A):
    scope = max(A) + 1
    C = [0] * scope
    for x in A:
        C[x] += 1
    pos = 0
    A[:] = []
    for number in range(scope):
        A += [number] * C[pos]
        pos += 1

A = [1, 2, 3, 3, 1, 1, 2, 1, 0, 3, 2, 1, 0]
SimpleCountingSort(A)
print(A)

"""
Поразрядная сортировка
"""

A = [12, 5, 664, 63, 5, 73, 93, 127, 432, 64, 34]
length = len(str(max(A)))
rang = 10
for i in range(length):
      B = [[] for k in range(rang)]
      for x in A:
            figure = x // 10**i % 10
            B[figure].append(x)
      A = []
      for k in range(rang):
            A = A + B[k]

print(A)
