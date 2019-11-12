from sys import argv

script_name, time, salary, bonus = argv

print(f'Зарплата сотрудника - {float(time)*float(salary)+float(bonus)}')