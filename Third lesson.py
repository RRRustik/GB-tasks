#1
"""
number1 = int(input("Введите любое первое число : "))
number2 = int(input("Введите любое второе число: "))

def calc(number1, number2):
    a = number1 / number2
    return a
print(calc(number1,number2)) #Почему он подчеркивает?

"""

#2
""" 
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой."""
"""
def personal_data(name, surname, birthday, Registration, email, tel):
    return f'{name} {surname} {birthday} {Registration} {email} {tel}'

n = input("Введите имя: ")
print(personal_data(name = n, surname = "Ryz", birthday = "12oct", Registration = "Moscow", email = "GBmail", tel = 84958505500)) # При написании почты как можно заменить точку?
"""


#3
""" 
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""
"""
number1 = int(input("Введите любое число 1: "))
number2 = int(input("Введите любое число 2: "))
number3 = int(input("Введите любое число 3: "))

def my_func(number1, number2, number3):
    #m = max(number1, number2, number3)
    n = min(number1, number2, number3)
    sum = number1 + number2 + number3
    max2 = sum - n
    return max2
print(my_func(number1, number2, number3))
"""
#4
"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень."""

x = int(input("Действительное положительное число "))
y = int(input("Целое отрицательное число "))

def my_func(x,y):
    #1calc = x**y
    i = 2
    calc = 1/x
    while i <= -y:
        calc = calc * 1/x
        i += 1
    return calc
print(my_func(x,y))

#6
"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""
"""
words = input("Введите несколько слов из латински букв в нижнем регистре через пробел: ")

def int_func(words):
    return words.title()

print(int_func(words))
"""