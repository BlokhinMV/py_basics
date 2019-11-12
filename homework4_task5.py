from functools import reduce

def multiply(el_1, el_2):
    return el_1 * el_2

my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Список чисел: {my_list}')
print(f'Произведение чисел в списке: {reduce(multiply, my_list)}')