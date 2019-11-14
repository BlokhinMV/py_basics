my_file = open('file1.txt', 'w')
string = None
while string != '':
    string = input('Введите строку для записи в фаил, для завершения - нажмите Enter')
    print(string, file=my_file)
my_file.close()
print('Запись файла завершена')