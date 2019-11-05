def my_func(arg1, arg2, arg3):
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        arg3 = int(arg3)
    except ValueError:
        print('Ошибка: Вы должны были ввести числа')
        return 'не определима, исправьте ошибку ввода'
    my_list = sorted([arg1, arg2, arg3])
    return my_list[-1] + my_list[-2]

arg1 = input('Введите первое число: ')
arg2 = input('Введите второе число: ')
arg3 = input('Введите третье число: ')
print(f'Сумма двух наибольших чисел: {my_func(arg1, arg2, arg3)}')
