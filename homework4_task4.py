u_list = input('Введите список чисел, разделяя их пробелом').split()
print(f'Исходный список: {u_list}')

new_list = [el for el in u_list if u_list.count(el) == 1]
print(f'Результат работы программы: {new_list}')