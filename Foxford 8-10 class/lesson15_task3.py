""" Самое частое слово в файле

Текстовый файл состоит из слов, записанных строчными буквами латинского алфавита, разделенных пробелами. Иных символов, кроме букв, пробелов и концов строк в файле нет.

Посчитайте, какое слово в этом файле встречается чаще всего. Выведите это слово. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Входные данные

Входные данные к этой задаче записаны в файле input.txt. Размер файла не превосходит 1 МБ.

Выходные данные
Программа должна вывести в файл output.txt искомое слово.

"""


dist = {}
fin = open("input3.txt")
fout = open("output3.txt", 'w')

sp = fin.read().split()

for key in sp:
    dist[key] = dist.get(key, 0) + 1

# print(sorted(dist, key=dist.get, reverse=True)[0])
# вообще не понял как это работает
res = min(dist.items(), key=lambda x: (-x[1], x[0]))[0]
print(res)

fin.close()
fout.close()