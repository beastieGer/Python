""" Количество различных слов в файле

Ограничение по времени работы программы: 1 секунда

Текстовый файл состоит из слов, записанных строчными буквами латинского алфавита, разделенных пробелами. Иных символов, кроме букв, пробелов и концов строк в файле нет. 

Посчитайте, сколько различных слов содержится в этом файле (если одно слово встречается несколько раз, то его нужно посчитать только один раз).

Входные данные

Входные данные к этой задаче записаны в файле input.txt. Размер файла не превосходит 1 МБ.

Выходные данные

Программа должна вывести в файл output.txt количество различных слов во входном файле.

"""

dist = {}

fin = open('input.txt')
fout = open('output.txt', 'w')
sp = fin.read().split()

for key in sp:
    dist[key] = dist.get(key, 0) + 1

fout.write(str(len(dist.keys())) + '\n')


fin.close()
fout.close()