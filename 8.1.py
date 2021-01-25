"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию (проверку на корректность) числа, месяца и года
(например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""

import time

class Data:
    def __init__(self, data_dmy):
        self.data_dmy = str(data_dmy)


    @classmethod
    def type_method(cls, data_dmy):
        data_dmy = data_dmy.split('-')
        day = int(data_dmy[0])
        month = int(data_dmy[1])
        year = int(data_dmy[2])
        #return day, month, year
        print(day)
        print(month)
        print(year)

    @staticmethod
    def validity_method(dmy):
        dmy = dmy.split('-')

        if ((int(dmy[0]) >= 0 and int(dmy[0]) <= 31) and (int(dmy[1]) == 1 or int(dmy[1]) == 3 or int(dmy[1]) == 5 or int(dmy[1]) == 7 or int(dmy[1]) == 8 or int(dmy[1]) == 10 or int(dmy[1]) == 12)) or \
                ((int(dmy[0]) >= 0 and int(dmy[0]) <= 30) and (int(dmy[1]) == 4 or int(dmy[1]) == 6 or int(dmy[1]) == 9 or int(dmy[1]) == 11)) or \
                ((int(dmy[0]) >= 0 and int(dmy[0]) <= 28) and int(dmy[2])):

            print("Correct")
        else:
            print('Please check data')


Data.type_method('25-12-1988')
Data.validity_method('29-02-1990')
