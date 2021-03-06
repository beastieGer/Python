"""Задача Иосифа Флавия

100 человек стоят по кругу, им присвоены номера от 1 до 100. Они начинают считаться и
каждый 19-й по счету выходит из круга. Таким образом сначала из круга выйдут люди с номерами 19, 38, 57, 76, 95, затем счет перейдет на начало круга и следующим выйдет человек с номером 14, а затем человек с номером 34 (так как человека с номером 19 уже не будет).

Определите номер человека, который последним останется в кругу.

"""

res = 0
for i in range(1, 100 + 1):
    res = (res + 19) % i

print(res + 1)

# Это нерекурсивная реализация рекурсивной формулы
# joseph(n, k) = (joseph(n-1, k) + k) % n;
