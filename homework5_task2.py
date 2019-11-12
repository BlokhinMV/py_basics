my_file = open('file2.txt', 'r')
i = 0 # счетчик строк
words = [] #список для сохранения длин строк
for line in my_file:
    i += 1
    words.append(len(line.split()))

print(f'В файле {i} строк')
i = 0
for j in words:
    i += 1
    print(f'Количество слов в {i}-й строке - {j}')

my_file.close()