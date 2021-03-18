ЗАДАНИЕ:
1)Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в 
часах*ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
2)Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Подсказка: элементы, удовлетворяющие условию,
оформить в виде списка. Для формирования списка использовать генератор. Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
3)Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку. Подсказка: использовать функцию range() и генератор.
4)Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке
их следования в исходном списке. Для выполнения задания обязательно использовать генератор. Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
5)Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо 
получить результат вычисления произведения всех элементов списка. Подсказка: использовать функцию reduce().
6)Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие
его завершения. Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
7)Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна
вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до
n!. Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

РЕШЕНИЕ:
1)
from sys import argv


def sale():
    try:
        return (lambda hour, rate, prem: hour * rate + prem)(*[float(_) for _ in argv[1:4]])
    except ValueError:
        print("ValueError: could not convert string to float.")
    except TypeError:
        print("TypeError: missing required positional argument.")


print(sale())
__________________________________________________________________________________________________________________________________________________________________________
2)
import random

list1 = random.sample(range(1, 200), 10)
print(list1)
list1.insert(0, list1[0] + 1)
list2 = [list1[i] for i in range(1, len(list1)) if list1[i - 1] < list1[i]]

print(list2)
__________________________________________________________________________________________________________________________________________________________________________
3)
print(f"Числа,кратные 20 или 21 - {[i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]}")
__________________________________________________________________________________________________________________________________________________________________________
4)
list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"first list: {list1}")
list2 = [i for i in list1 if list1.count(i) < 2]
print(f"second list: {list2}")
__________________________________________________________________________________________________________________________________________________________________________
5)
from functools import reduce

list1 = [el for el in range(100, 1001) if el % 2 == 0]
print(list1)
a = reduce(lambda x, y: x * y, list1)
print(a)
__________________________________________________________________________________________________________________________________________________________________________
6)
from itertools import count, cycle


def func(first_number, last_number):
    for el in count(first_number):
        if el > last_number:
            break
        else:
            print(el)


def func1(my_list, iteration):
    c = 0
    iter = cycle(my_list)
    while c < iteration:
        print(next(iter))
        c += 1


func(first_number=int(input("first number: ")), last_number=int(input("last number: ")))
func1(my_list=[str(i) for i in input("Enter list items separated by a space: ").split()],
      iteration=int(input("number of iterations: ")))
__________________________________________________________________________________________________________________________________________________________________________
7)
from math import factorial


def fact(a):
    for counter in range(1, a + 1):
        yield factorial(counter)


if __name__ == "__main__":

    try:
        chislo = int(input("Enter a number more than 1: "))
        if chislo < 1:
            print("Number less than 1")
            exit()

    except ValueError:
        print("It is not a number")
        exit()

    for el in fact(chislo):
        print(el)
