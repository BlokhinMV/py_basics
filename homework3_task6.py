def int_func(word):
    return word.capitalize()

word = input('Введите слово: ')
print(f'Результат преобразования - {int_func(word)}')

string = input('Введите строку, разделяя слова пробелами: ').split()
res_string = []
for i in string.copy():
    res_string.append(int_func(i))
string = ' '.join(res_string)
print(f'Результат преобразования - {string}')