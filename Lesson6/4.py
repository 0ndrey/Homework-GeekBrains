class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is started')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Speed of {self.name} is higher than allow for town car')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Speed of {self.name} is higher than allow for work car')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


subaru = SportCar(100, 'Red', 'Subaru')
mazda = TownCar(30, 'White', 'Mazda')
ford = WorkCar(300, 'Rose', 'Ford')
dodge = PoliceCar(110, 'Blue',  'Dodge')
mazda.turn("left")
mazda.show_speed()
subaru.show_speed()
ford.show_speed()
ford.turn("right")
ford.go()
subaru.stop()

