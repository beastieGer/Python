"""ФИО

Напишите программу, которая преобразует строку, содержащую имя, отчество и фамилию
человека, к форме
<фамилия> <инициалы>

Входные данные
Входная строка содержит имя, отчество и фамилию, разделённые одиночными пробелами.

Выходные данные
Программа должна вывести в одной строке сначала фамилию, а потом (через пробел) –
инициалы.

"""

name, middle_name, family = input().split()

print(family, name[0]+'.', middle_name[0]+'.')

