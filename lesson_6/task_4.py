class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(direction)

    def show_speed(self):
        print(f'current speed: {self.speed}')


class TownCar(Car):
    def __init__(self, name, color, is_police=False):
        super().__init__(name, color, is_police)
        print('this is a city car')

    def show_speed(self):
        if self.speed > 60:
            print(f'current speed: {self.speed} speed limit exceeded')
        else:
            print(f'current speed: {self.speed}')


class WorkCar(Car):
    def __init__(self, name, color, is_police=False):
        super().__init__(name, color, is_police)
        print('this is a work car')

    def show_speed(self):
        if self.speed > 40:
            print(f'current speed: {self.speed} speed limit exceeded')
        else:
            print(f'current speed: {self.speed}')


class SportCar(Car):
    def __init__(self, name, color, is_police=False):
        super().__init__(name, color, is_police)
        print('this is a sport car')


class PoliceCar(Car):
    def __init__(self, name, color, is_police=False):
        super().__init__(name, color, is_police)
        print('this is a police car')


town_car = TownCar('BMW', 'black')
town_car.speed = 50
town_car.show_speed()
town_car.speed = 70
town_car.show_speed()

work_car = WorkCar('MAN', 'white')
work_car.speed = 35
work_car.show_speed()
work_car.speed = 45
work_car.show_speed()

sport_car = SportCar('FERRARI', 'red')
sport_car.speed = 200
sport_car.show_speed()

police_car = PoliceCar('FORD', 'black', True)
police_car.speed = 80
police_car.show_speed()
