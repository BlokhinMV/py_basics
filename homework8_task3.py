class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

usr_inp = None
list = []

print('Введите число. Для завершения ввода нажмите Enter')
while True:
    usr_inp = input()
    if usr_inp != '':
        try:
            flag = usr_inp.isdigit()
            if not flag:
                raise OwnError('Вы ввели не число, попробуйте еще раз')
        except OwnError as err:
            print(err)
        else:
            list.append(usr_inp)
    else:
        break

print(f'Список введенных чисел: {" ".join(list)}')