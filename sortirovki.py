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