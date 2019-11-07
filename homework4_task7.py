from math import factorial

# Вариант 1 - Количество выводимых чисел ограничено в функции
def fibo_gen(i=1):
    for el in range(i, i + 15):
        yield factorial(el)

for el in fibo_gen():
    print(el, end=' ')

# Вариант 2 - Бесконечный генератор, ограничение вывода - внутри цикла
from itertools import count
def fibo_gen1(i=1):
    for el in count(i):
        yield factorial(el)

print()
c = 0
for el in fibo_gen1():
    if c >= 15:
        break
    print(el, end=' ')
    c += 1
