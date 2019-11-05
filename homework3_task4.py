def my_func(x, y):
    '''вариант с оператором **

    В функции проверяется соответствие числа и показателя степени типам,
    а так же соответствие - число положительное, показатель отрицательный
    После чего происходит возведение в степень

    '''

    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Необходимо ввести числа')
        return 'Не может быть расчитано'
    if x <= 0 or y >= 0:
        print('Необходимо ввести положительное число и отрицательный показатель')
        return 'Не может быть расчитано'
    else:
       return x ** y

def my_func2(x, y):
    '''вариант с циклом'''
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Необходимо ввести числа')
        return 'Не может быть расчитано'
    if x <= 0 or y >= 0:
        print('Необходимо ввести положительное число и отрицательный показатель')
        return 'Не может быть расчитано'
    else:
        result = 1
        for i in range(-y):
            result *= x
        result = 1 / result
    return result

x = input('Введите положительное число: ')
y = input('Введите отрицательную степень, в которую его необходимо возвести: ')
print(f'{x} в степени {y} - {my_func(x, y)}')
print(f'{x} в степени {y} - {my_func2(x, y)}')
print('Выполнение программы завершено')
