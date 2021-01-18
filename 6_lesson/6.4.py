
"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f' {self.name} поехала')

    def stop(self):
        print(f' {self.name} остановилась')

    def turn(self, direction):
        print(f' {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысила скорость')
        else:
            print(f'Скорость авто {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превысила скорость')
        else:
            print(f'Скорость авто {self.speed}')

class PoliceCar(Car):
    pass

WC = WorkCar(50, 'Green', 'VW', False)
print(WC.go(), WC.stop(), WC.turn('налево'), WC.turn('направо'), WC.show_speed())

PC = PoliceCar(40, 'Blue', 'Ford', True)
print(WC.go(), WC.stop(), WC.turn('налево'), WC.turn('направо'), WC.show_speed())

SC = SportCar(200, 'Red', 'Ferrari', False)
print(WC.go(), WC.stop(), WC.turn('налево'), WC.turn('направо'), WC.show_speed())

TC = TownCar(20, 'Black', 'BMW', False)
print(WC.go(), WC.stop(), WC.turn('налево'), WC.turn('направо'), WC.show_speed())


