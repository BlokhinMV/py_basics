with open('file5.txt', 'w') as my_file:
    line = input('Введите числа, разделяя их пробелами: \n')
    my_file.write(line)

with open('file5.txt', 'r') as my_file:
    numbers = my_file.read()
    print(f'Числа: {numbers}')
    print(f'Cумма чисел в файле: {sum(map(int,numbers.split()))}')