with open('file3.txt', 'r') as my_file:
    staff = my_file.read().split('\n')
low_salary = []
sum_salary = 0
for i in staff:
    i = i.split()
    if int(i[1]) < 20000:
        low_salary.append(i[0])
    sum_salary += int(i[1])
low_salary = ', '.join(low_salary)
print(f'Сотрудники с зарплатой ниже 20000: {low_salary}')
print(f'Средняя величина дохода сотрудников: {sum_salary / len(staff)}')
