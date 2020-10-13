from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for item in cycle(self.__color):
            print(item)
            if item == 'red':
                sleep(7)
            elif item == 'yellow':
                sleep(2)
            else:
                sleep(9)


traffic_light = TrafficLight()
traffic_light.running()
