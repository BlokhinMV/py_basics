n = input('Введите число: ')

nn = int(n * 2)
nnn = int(n * 3)

print(f'Сумма чисел {n}+{nn}+{nnn} = {int(n) + nn + nnn}')


# Альтернативный вариант, без конкантенации строк:
n = int(input('Введите число: '))

nn = 10 * n + n
nnn = 100 * n + nn

print(f'Сумма чисел {n}+{nn}+{nnn} = {n + nn + nnn}')