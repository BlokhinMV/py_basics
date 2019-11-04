# через список
seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

while True:
    month = int(input('Введите номер месяца: '))
    if month < 1 or month > 12:
        print('Вы ошиблись! Номер месяца должен быть от 1 до 12')
    else:
        break

print(f'Ваш месяц относится ко времени года {seasons[month - 1]}')

# через словарь
seasons = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

while True:
    month = int(input('Введите номер месяца: '))
    if month < 1 or month > 12:
        print('Вы ошиблись! Номер месяца должен быть от 1 до 12')
    else:
        break

print(f'Ваш месяц относится ко времени года {seasons[month]}')