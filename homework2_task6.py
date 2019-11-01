goods = []
i = 1
pos = int(input('Введите количество позиций для внесения в базу'))

while i <= pos:
    name = input('Введите название: ')
    price = input('Введите цену: ')
    quantity = input('Введите количество: ')
    mes = input('Введите единицу измерения: ')
    var_dict = {'название': name, 'цена': price, 'количество': quantity, 'ед.': mes}
    goods.append((i, var_dict))
    i += 1

names = set()
prices = set()
quants = set()
mess = set()
for pos, dic in goods:
    names.add(dic.get('название'))
    prices.add(dic.get('цена'))
    quants.add(dic.get('количество'))
    mess.add(dic.get('ед.'))
analytics = {'название': list(names), 'цена': list(prices), 'количество': list(quants), 'ед.': list(mess)}

key = None
while key != 'exit':
    key = input('Введите характеристику, по которой необходимо вывести перечень позиций, для завершения введите "exit": ')
    if key == 'exit':
        break
    else:
        print(analytics.get(key))