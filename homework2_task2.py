my_list = []
el = None

while el != 'exit':
    el = input('Введите элемент списка, для выхода введите "exit"')
    my_list.append(el)
my_list.remove('exit')

for el in range(1, len(my_list), 2):
    my_list[el - 1], my_list[el] = my_list[el], my_list[el - 1]

print(my_list)