my_list = ['строка', 5, 5.25, None, False, ('кор', 'теж'), {1: 'январь', 2: 'февраль'}]

for i, el in enumerate(my_list):
    print(f'Тип элемента {i} - {type(el)}')