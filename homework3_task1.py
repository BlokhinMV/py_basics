def division(arg_1, arg_2):
    try:
        div = arg_1 / arg_2
    except ZeroDivisionError:
        print('Ошибка: Знаменатель не может быть равен нулю!')
        return 'не может быть определен, исправьте ошибку'
    else:
        return div

try:
    arg_1 = int(input('Введите числитель дроби: '))
    arg_2 = int(input('Введите знаменатель дроби: '))
except ValueError:
    print('Необходимо вводить только числа!')
else:
    print(f'Результат деления - {division(arg_1, arg_2)}')
print('Выполнение программы завершено')