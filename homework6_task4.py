from termcolor import colored
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{colored(self.name, self.color)} started movement'
    def stop(self):
        return f'{colored(self.name, self.color)} has stopped'
    def turn(self, direction):
        return f'{colored(self.name, self.color)} has turned {direction}'
    def show_speed(self):
        return f'{colored(self.name, self.color)} is cruising at {self.speed}km/h'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} is cruising at {self.speed}km/h.', end=' ')
        if self.speed > 60:
            return 'That speed is excessive for a town car!'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} is cruising at {self.speed}km/h.', end=' ')
        if self.speed > 40:
            return 'That speed is excessive for a work car!'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

tc = TownCar(55, 'white', 'Volkswagen', False)
wc = WorkCar(50, 'yellow', 'GAZ', False)
sc = SportCar(310, 'magenta', 'Maserati', False)
pc = PoliceCar(100, 'blue', 'Lada', True)


print(f'While {pc.show_speed()}, {sc.turn("right")}')
print(wc.show_speed())
print(f'Is {pc.name} a police car? - {pc.is_police}')
print(f'When {wc.go()}, {sc.stop()}, so {tc.turn("left")} and {pc.show_speed()}')