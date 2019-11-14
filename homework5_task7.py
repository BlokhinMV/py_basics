import json
profits = dict()
total_profit = 0
i = 0
with open('file7.txt', 'r') as my_file:
    for line in my_file:
        name, ownership, profit, expenses = line.split()
        profits[name] = int(profit) - int(expenses)
        if profits.get(name) >= 0:
            total_profit += profits.get(name)
            i += 1
    try:
        av_profit = total_profit / i
    except ZeroDivisionError:
        av_profit = 'убыток'
    av_profits = {'Средняя прибыль:': round(av_profit, 2)}
    result = [profits, av_profits]
print(f'Прибыль каждой фирмы и средняя:\n{result}')

with open('file7.json', 'w') as w_file:
    json.dump(result, w_file)
