u_list = input('Введите список чисел, разделяя их пробелом').split()
print(f'Исходный список: {u_list}')

new_list = [u_list[i] for i in range(1, len(u_list)) if u_list[i] > u_list[i - 1]]
print(f'Результат работы программы: {new_list}')