from time import sleep
from itertools import cycle
from termcolor import colored
class Trafficlight:
    __color = ['red', 'yellow', 'green', 'yellow']
    def running(self):
       for light in cycle(Trafficlight.__color):
            print(f'The traffic light is now {colored(light, light)}')
            if light == 'red':
                sleep(7)
            elif light == 'yellow':
                sleep(2)
            else:
                sleep(9)

t = Trafficlight()
t.running()