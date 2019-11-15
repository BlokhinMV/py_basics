class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self, gauge):
        mass = self._length * self._width * gauge * 25 / 1000
        print(round(mass))

r = Road(5000, 20)
r.count_mass(5)