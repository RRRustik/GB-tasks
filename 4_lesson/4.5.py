"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

even_list = []

for num in range(100, 1001):
    if num % 2 == 0:
        even_list.append(num)

mult = reduce(lambda x, y: x * y, even_list)

print(mult)