ЗАДАНИЕ:
1)Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
2)Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
3)Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не 
фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, 
сформированный список с числами выводится на экран. Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
4)Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы
— конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5)Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
6)Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных. Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках 
по ООП.
7)Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного 
результата.

РЕШЕНИЕ:
1)
class Date:
    date: str

    def __init__(self, date: str = 'dd-mm-yyyy'):
        self.date = date

    @classmethod
    def date_get(cls, date):
        try:
            return [int(el) for el in date.split('-')]
        except ValueError:
            print("Wrong date")
            exit()

    @staticmethod
    def date_validate(date: list):
        day, month, year = date
        if 0 < day < 32 and 0 < month < 13:
            return f'Date {day:02d}:{month:02d}:{year:0004d} is correct'
        else:
            return f'Date {day:02d}:{month:02d}:{year:0004d} incorrect'


user_date = input('Input date dd-mm-yyyy: ')
val_date = Date.date_get(user_date)
print(Date.date_validate(val_date))
________________________________________________________________________________________________________________________________________________________________________
2)
class OopsdividerByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    devidend = int(input('Input Dividend: '))
    divider = int(input('Input Divider: '))
    if not divider:
        raise OopsdividerByZero('The Divider cannot be zero ')
    print(f'Результат {devidend / divider}')

except ValueError:
    print("It's not a a number")
except OopsdividerByZero as error:
    print(error)
________________________________________________________________________________________________________________________________________________________________________
3)
class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


list1 = []

print('To stop the program write "stop"')
while True:
    in_data = input('Enter a number: ').lower()
    try:
        if in_data.isdigit() == False and in_data != 'stop':
            raise Error('Enter a numbers!')
        elif in_data == 'stop':
            print(list1)
            quit()
    except Error as err:
        print(err)
    else:
        list1.append(in_data)
________________________________________________________________________________________________________________________________________________________________________
4)
class OfficeEquipmentWarehouse:
    """Класс склад оргтехники"""
    print("\nСклад оргтехники")


class OfficeEquipment:
    """Базовый класс оргтехники"""

    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    """Класс принтер"""
    amount_pr = 0

    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1

    @staticmethod
    def name():
        return "<<Принтер>>"

    def type_printer(self):
        return self.pr_type

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}  \tтип принтера: {}".format(self.producer, self.color, self.pr_type)


class Scanner(OfficeEquipment):
    """Класс сканер"""
    amount_sc = 0

    def __init__(self, producer, color, sc_sensor):
        super().__init__(producer, color)
        self.sc_sensor = sc_sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return "<<Сканер>>"

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {} \tтип сенсора: {}".format(self.producer, self.color, self.sc_sensor)


class Xerox(OfficeEquipment):
    """Класс ксерокс"""
    amount_x = 0

    def __init__(self, producer, color, xer_wi_fi):
        super().__init__(producer, color)
        self.xer_wi_fi = xer_wi_fi
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return "<<Ксерокс>>"

    def wi_fi_module(self):
        return self.xer_wi_fi

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}   \tWi-Fi модуль: {}".format(self.producer, self.color, self.xer_wi_fi)


p = Printer('Canon', 'white', 'лазерный')
p2 = Printer('Canon', 'black', 'лазерный')
print(p.name(), p.amount_pr, "шт")
print(p.__str__())
print(p2.__str__())
s = Scanner('Kyocera', 'black', 'CCD')
s2 = Scanner('Canon', 'black', 'CCD')
print(s.name(), s.amount_sc, "шт")
print(s.__str__())
print(s2.__str__())
x = Xerox('Xerox', 'red', 'нет')
print(x.name(), x.amount_x, "шт")
print(x.__str__())
________________________________________________________________________________________________________________________________________________________________________
7)
class Complex:
    real: int
    compl: int

    def __init__(self, real, compl):
        self.real = real
        self.compl = compl

    def __str__(self):
        if self.compl > 0:
            return f"{self.real}+{self.compl}i"
        else:
            return f"{self.real}{self.compl}i"

    def __add__(self, other):
        real_var = self.real + other.real
        compl_var = self.compl + other.compl
        return Complex(real_var, compl_var)

    def __mul__(self, other):
        real_var = self.real * other.real
        compl_var = self.compl * other.compl
        return Complex(real_var, compl_var)


var1 = Complex(-6, -1)
var2 = Complex(5, 2)
print(f"first number: {var1}")
print(f"second number: {var2}")
print(f"sum = {var1 + var2}")
print(f"multiplication = {var1 * var2}")
