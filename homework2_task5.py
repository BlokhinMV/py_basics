rate = [155, 101, 28, 10, 10, 3, 3, 3, 2]

while True:
    el = input('Введите новый элемент рейтинга, для выхода введите exit')
    if el == 'exit':
        break
    else:
        el = int(el)

    if el in rate:
        pos = rate.index(el)
        quant = rate.count(el)
        rate.insert(pos + quant, el)
    elif el < rate[-1]:
        rate.append(el)
    else:
        for i in range(len(rate)):
            if el > rate[i]:
                rate.insert(i, el)
                break
    print(rate)