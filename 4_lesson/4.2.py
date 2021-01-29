"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

number_list = [23, 25, 6, 3, 75, 32, 45, 56, 13, 41]

new_number_list = []

for number in range(len(number_list)):
    if number_list[number-1] < number_list[number]:
        new_number_list.append(number_list[number])

print(new_number_list)