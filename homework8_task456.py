class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Storage:
    def __init__(self):
        self.printers = dict()
        self.scaners = dict()
        self.copiers = dict()

    def add_unit(self, type, name, quantity, cost):
        if type == 'printer':
            self.printers.update(Printer(name, quantity, cost).unit)
        elif type == 'scaner':
            self.scaners.update(Scaner(name, quantity, cost).unit)
        elif type == 'copier':
            self.copiers.update(Copier(name, quantity, cost).unit)
        else:
            print('wrong type!')

    def remove_unit(self):
        type = input('Input type of needed device: ')
        try:
            name = input('Input model name: ')
            if name not in self.printers.keys() and name not in self.scaners.keys() and name not in self.copiers.keys():
                raise MyError('No such model at the storage')
        except MyError as err:
            print(err)

        try:
            quantity = input('Enter needed quantity: ')
            if not quantity.isdigit():
                raise MyError('You should enter number!')
        except MyError as err:
            print(err)
            quantity = 0
        else:
            quantity = int(quantity)

        if type == 'printer':
            self.printers[name] = self.printers.get(name, quantity) - quantity
        elif type == 'scaner':
            self.scaners[name] = self.scaners.get(name, quantity) - quantity
        elif type == 'copier':
            self.copiers[name] = self.copiers.get(name, quantity) - quantity
        else:
            print('wrong type!')
    @property
    def show_storage(self):
        print('На складе имеются в наличии:')
        print(f'Принтеры: {self.printers}')
        print(f'Сканеры: {self.scaners}')
        print(f'Копиры: {self.copiers}')

class OfficeTech:
    def __init__(self,  name, quantity, cost):
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.unit = {name: quantity}

class Printer(OfficeTech):
    def __init__(self, name, quantity, cost):
        self.type = 'printer'
        super().__init__(name, quantity, cost)
    @staticmethod
    def to_print(pgs):
        return f'Printing {pgs} pages'

class Scaner(OfficeTech):
    def __init__(self, name, quantity, cost):
        self.type = 'scaner'
        super().__init__(name, quantity, cost)

class Copier(OfficeTech):
    def __init__(self, name, quantity, cost):
        self.type = 'copier'
        super().__init__(name, quantity, cost)

s = Storage()
u1 = Printer('Cannon', 5, 5000)
print(u1.to_print(10))
s.add_unit('printer', 'Cannon', 10, 5000)
s.add_unit('scaner', 'Epson', 15, 2500)
s.add_unit('copier', 'Xerox', 2, 10000)
s.add_unit('printer', 'Brother', 3, 11500)
s.remove_unit()
s.show_storage
