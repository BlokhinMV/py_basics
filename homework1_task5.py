income = float(input('Введите значение выручки фирмы: ')) #прибыль может быть и не целым числом, поэтому float
expenses = float(input('Введите значение издержек: '))

if income > expenses:
    print('Фирма отработала с прибылью')
    profit = income - expenses
    print(f'Рентабельность прибыли - {(profit/income):0.2f}')
    staff = int(input('Введите число сотрудников фирмы: '))
    print(f'Рентабельность в расчете на одного сотрудника - {(profit / staff):0.2f}')

elif income == expenses:
    print('Фирма отработала в точке безубыточности')

else:
    print('Фирма отработала с убытком')