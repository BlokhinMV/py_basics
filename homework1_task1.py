var_str = 'Строка'
var_bool = 15 is 15
var_int = 15
var_float = 3.563

print(f'Переменные - строковая: "{var_str}", логическая: {var_bool}, целочисленная: {var_int}, с плавающей точкой: {var_float}')

var_str = input('Введите любые символы: ')
var_bool = bool(input('Введите "True", "False" или логическое выражение: '))
var_int = int(input('Введите целое число: '))
var_float = float(input('Введите дробное число: '))

print(f'Переменные пользователя - строковая: "{var_str}", логическая: {var_bool}, целочисленная: {var_int}, с плавающей точкой: {var_float}')