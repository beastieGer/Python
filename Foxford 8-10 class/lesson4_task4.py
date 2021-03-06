"""Взаимно простые числа

Два числа называются взаимно простыми, если они не имеют общего натурального делителя,
кроме 1. Иными словами, их наибольший общий делитель равен 1.
Найдите количество шестизначных чисел, взаимно простых с числом 70.
ответ - 308571

"""

aa = 70
bb = 100000
count = 0
while bb < 1000000:
    a = aa
    b = bb
    while b != 0:
        a, b = b, a % b
    if a == 1:
        count += 1
    bb += 1
print(count)
