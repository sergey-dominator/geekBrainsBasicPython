class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} has started up')

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f'{self.name} is riding with following speed: {self.speed}')


class TownCar(Car):
    limit_speed = 60

    def show_speed(self):
        if self.speed > TownCar.limit_speed:
            print(f'{self.name} is riding with speed bigger than {TownCar.limit_speed}. Please slow down')
        else:
            super().show_speed()


class WorkCar(Car):
    limit_speed = 40

    def show_speed(self):
        if self.speed > WorkCar.limit_speed:
            print(f'{self.name} is riding with speed bigger than {WorkCar.limit_speed}. '
                  f'You have to follow driving rules')
        else:
            super().show_speed()


fast_town_car = TownCar(150, "RED", "Marty", False)
slow_town_car = TownCar(40, "BLUE", "Peter", False)
print(f'The name of fast town car is {fast_town_car.name}')
print(f'The name of slow town car is {slow_town_car.name}')
fast_town_car.show_speed()
slow_town_car.show_speed()

fast_work_car = WorkCar(70, "YELLOW", "Canny", False)
slow_work_car = WorkCar(20, "GREEN", "Dan", False)
fast_work_car.show_speed()
slow_work_car.show_speed()
