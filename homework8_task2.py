class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_num = int(input('Введите числитель дроби: '))
inp_cons = int(input('Введите знаменатель дроби'))
try:
    if inp_cons == 0
        raise OwnError('Деление на ноль недопустимо')
    result = inp_num / inp_cons
except OwnError as err:
    print(err)
else:
    print(round(result, 2))