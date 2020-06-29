class Car:

    def __init__(self, color: str, name: str, speed: int = 0, is_police: bool = False):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = is_police

    def go(self, speed, name):
        self.speed = speed
        print(f'Car {name} start movement with speed: {speed}')

    def stop(self):
        print(f'Car {self.name} has stopped')
        self.speed = 0

    def turn(self, direction):
        print(f'Car {self.name} turn on {direction}')

    def show_speed(self):
        print(f'Current {self.name} speed: {self.speed}')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)
        Car.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print('Speed too high! Car should decrease speed')
            print(f'Car {self.name} speed: {self.speed}')
        else:
            print(f'Car {self.name} speed: {self.speed}')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)
        Car.is_police = False
    max_speed = 280


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        super().__init__(color, name)
        Car.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print('Speed too high! Car should decrease speed')
            print(f'Car {self.name} speed: {self.speed}')
        else:
            print(f'Car {self.name} speed: {self.speed}')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True

car1 = TownCar('Green', 'Opel Astra')
car2 = WorkCar('Grey', 'Lada Largus')
car3 = SportCar('Red', 'Nissan Z350')
car4 = PoliceCar('White&Blue', 'Nissan Skyline')

car1.go(65, car1.name)
print(f'Is police? {car1.is_police}')
print('-'*10)
car2.go(45, car2.name)
print('-'*10)
car3.go(70, car3.name)
print('-'*10)
car4.go(80, car4.name)
print(f'Is police? {car4.is_police}')
print('-'*10)
car1.stop()
print('-'*10)
car1.show_speed()
print('-'*10)
car2.show_speed()
print('-'*10)
car3.show_speed()
print('-'*10)
car4.show_speed()

car3.turn('left')
