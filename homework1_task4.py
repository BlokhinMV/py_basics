number = int(input('Введите целое положительное число: '))

max_num = 0

while number > 0:
    num = number % 10
    number = number // 10
    if num > max_num:
        max_num = num

print(f'Самая большая цифра в Вашем числе: {max_num}')