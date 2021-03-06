ЗАДАНИЕ:
1)Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы. Следующий шаг — реализовать перегрузку метода str() для вывода
матрицы в привычном виде. Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой
строки второй матрицы и т.д.
2)Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу 
этих методов на реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
основных классов проекта, проверить на практике работу декоратора @property.
3)Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),умножение (mul()),
деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление
клеток, соответственно. Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток. Вычитание. Участвуют две 
клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение. Умножение. Создается общая
клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток. Деление. Создается общая клетка из двух. Число ячеек общей клетки
определяется как целочисленное деление количества ячеек этих двух клеток. В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество 
ячеек в ряду. Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно 
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12, 
количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****.

РЕШЕНИЕ:
1)
class Matrix:
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summa = other.mat[i][j] + self.mat[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.mat[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[1, 3, 6], [1, -2, 7], [3, 2, 4]]
b = [[1, 2, 3], [4, 9, -7], [6, 3, 1]]
m = Matrix(a)
mm = Matrix(b)

print("\nМатрица 1")
print(m.__str__(), "\n")

print("Матрица 2")
print(mm.__str__(), "\n")

print("Сумма матриц")
print(m + mm)
________________________________________________________________________________________________________________________________________________________________________
2)
from abc import ABC, abstractmethod


class Apparel(ABC):
    def __init__(self, x):
        self._name = "Apparel"
        self._parameter_name = "Apparel parameter name"
        if x and (isinstance(x, int) or isinstance(x, float)):
            self.parameter = x
        else:
            self.parameter = 0
            self._parameter_name = f"Apparel parameter name = ERROR {str(x)}"
            print(self._parameter_name)

    def __str__(self):
        return f"{self._name} : {self._parameter_name} = {self.parameter}"

    @abstractmethod
    def consumption(self):
        return self.parameter


class Costume(Apparel):
    def __init__(self, x):
        super().__init__(x)
        self._name = "костюм"
        self._parameter_name = "рост"

    @property
    def consumption(self):
        return 2 * self.parameter + 0.3


class Coat(Apparel):
    def __init__(self, x):
        super().__init__(x)
        self._name = "пальто"
        self._parameter_name = "размер"

    @property
    def consumption(self):
        return self.parameter / 6.5 + 0.5


my_coat = Coat(2)
print(my_coat)
my_costume = Costume(5)
print(my_costume)

print()
print(f"Суммарный расход ткани :  {my_coat.consumption + my_costume.consumption:>5.02f} кв.метров")
________________________________________________________________________________________________________________________________________________________________________
3)
class Cells:
    def __init__(self, chislo: int):
        self.chislo = chislo

    def __add__(self, other):
        return f"Сложение, размер клетки = {self.chislo + other.chislo}"

    def __sub__(self, other):
        return f"Вычитание, размер клетки = {self.chislo - other.chislo}" \
            if self.chislo - other.chislo > 0 else "Клетка исчезла"

    def __mul__(self, other):
        return f"Умножение, размер клетки равен = {self.chislo * other.chislo}"

    def __truediv__(self, other):
        return f"Деление, размер клетки равен = {self.chislo // other.chislo}"

    def make_order(self, cell_row):
        row_cell = ''
        for i in range(int(self.chislo / cell_row)):
            row_cell += '*' * cell_row + '\n'
        row_cell += '*' * (self.chislo % cell_row)
        return row_cell


cell_base = Cells(12)
cell_change = Cells(5)

print(cell_base + cell_change)
print(cell_base - cell_change)
print(cell_base * cell_change)
print(cell_base / cell_change)

print(f"Метод make_order():")
print(cell_base.make_order(5))
