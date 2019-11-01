user_str = input('Введите несколько слов: ')
my_list = user_str.split()

for i, el in enumerate(my_list):
    print(i, el[:10])