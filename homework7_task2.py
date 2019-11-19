from abc import ABC, abstractmethod
class AbstractClothes:
    @abstractmethod
    def __init__(self):
        pass

class Coat(AbstractClothes):
    def __init__(self, size):
        self.usage = size / 6.5 + 0.5

class Suit(AbstractClothes):
    def __init__(self, height):
        self.usage = 2 * height + 0.5

class Clothes:
    def __init__(self):
        self.usage = []
        self.total_usage = 0
    def add_coat(self, size):
        self.usage.append(Coat(size))
    def add_suit(self, height):
        self.usage.append(Suit(height))
    @property
    def common_usage(self):
        for el in self.usage:
            self.total_usage += el.usage
        return self.total_usage

c = Clothes()
c.add_coat(39)
c.add_suit(1.75)
c.add_suit(1.80)

print(f'Общий расход ткани: {c.common_usage} квадратных метров')