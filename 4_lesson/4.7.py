"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""

"""
generator = (param * param for param in range(5))

for el in generator:
    print(el)
"""
"""def generator():
    for el in (10, 20, 30):
        yield el

g = generator()
print(g)

for el in g:
    print(el)
"""
"""
from itertools import count
from math import factorial

def factorial_f():
    for el in count(1):
        yield factorial(el)


fact = factorial_f()
x = 0
print(fact)

for n in fact:
    if x < 15:
        print(n)
        x += 1
    else:
        break

"""

from itertools import count

def factorial_f(n):
    for num in count(1):
        k = 1
        c = 1
        while c < n:
            c += 1
            k = k * (c)
        yield k


fact = factorial_f(7)

for el in fact:
    print(el)
    break
