class Date:
    def __init__(self, date):
        Date.date = date
        Date.day = 0
        Date.month = 0
        Date.year = 0

    @classmethod
    def extract(cls):
        list = cls.date.split('-')
        cls.day, cls.month, cls.year = Date.check(list)

    @staticmethod
    def check(list):
        day = int(list[0]) if int(list[0]) > 0 and int(list[0]) <= 31 else print('Неверно введено число')
        month = int(list[1]) if int(list[1]) > 0 and int(list[1]) <= 12 else print('Неверно введен месяц')
        year = int(list[2]) if int(list[2]) > 2000 and int(list[2]) <= 2019 else print('Неверно введен год')
        return day, month, year


d = Date('12-01-1999')
d.extract()
print(f'День: {d.day:02d}')
print(f'Месяц: {Date.month:02d}')
print(f'Год: {Date.year}')
