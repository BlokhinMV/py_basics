def sum_numbers(list, quit):
    summ = 0
    for i in list:
        if i != 'q':
            try:
                summ += int(i)
            except ValueError:
                print('Необходимо вводить только числа')
                summ = 0
                quit = 0
                return summ, quit
        else:
            quit = 1
            break
    return summ, quit

result = 0
quit = 0

while quit != 1:
    string = input('Введите числа для суммирования, разделяя их пробелами, для выхода введите q').split()
    summ, quit = sum_numbers(string, quit)
    result += summ
    print(f'Сумма введенных чисел: {result}')

print('Работа программы завершена')