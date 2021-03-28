ЗАДАНИЕ:
1)Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода 
реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, 
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу 
примера, создав экземпляр и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
2)Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра 
класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: 
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.Проверить работу метода.Например:20м*5000м*25кг*5см=12500т
3)Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса 
Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на
реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
4)Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
5)Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
6)Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск 
отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из 
классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

РЕШЕНИЕ:
1)
import time


class TrafficLight:
    __traffic_light_color = "Светофор"

    def running(self):
        while True:
            print("Red")
            time.sleep(7)
            print("Yellow")
            time.sleep(2)
            print("Green")
            time.sleep(4)


var1 = TrafficLight()
var1.running()
________________________________________________________________________________________________________________________________________________________________________
2)
class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()
________________________________________________________________________________________________________________________________________________________________________
3)
class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        print(
            f'{self.get_full_name()} {self.position} Wage={self._income.get("wage") + self._income.get("bonus")}')


example = Position('Ivan', 'Petrov', 'Engineer', {"wage": 70000, "bonus": 40000})
example.get_total_income()
________________________________________________________________________________________________________________________________________________________________________
4-5)
from random import randint


class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = randint(10, 150)
        print(f"{self.name} {self.color} Поехал")

    def stop(self):
        self.speed = 0
        print(f"{self.name} {self.color} Остановился")

    def turn(self, direction):
        print(f"{self.name} {self.color} Повернул {direction}")

    def show_speed(self):
        print(f"{self.name} {self.color} Едет со скоростью {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости")


class SportCar(Car):
    def show_speed(self):
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


if __name__ == "__main__":
    sport_car = SportCar("black", "lamborghini")
    work_car = WorkCar("white", "audi")
    town_car = TownCar("red", "porsche")
    police_car = PoliceCar("black", "ford")

    sport_car.go()
    sport_car.show_speed()
    sport_car.turn("на право")
    sport_car.stop()
    print()

    work_car.go()
    work_car.show_speed()
    work_car.turn("на лево")
    work_car.stop()
    print()

    town_car.go()
    town_car.show_speed()
    town_car.turn("на лево")
    town_car.turn("на право")
    town_car.stop()
    print()

    police_car.go()
    police_car.show_speed()
    police_car.turn("на лево")
    police_car.turn("на лево")
    police_car.stop()
    print()
________________________________________________________________________________________________________________________________________________________________________
6)
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. Запуск отрисовки ручкой"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. Запуск отрисовки карандашом"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. Запуск отрисовки маркером"


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())

