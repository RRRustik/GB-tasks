"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Dress(ABC):

    def __init__(self, V):
        self.V = V

    def __add__(self, other):
        return Dress(self.V+other.V)

    @abstractmethod
    def abc_method(self):
        pass


class Coat(Dress):

    @property
    def coat_f(self):
        tiscon_c = self.V/6.5 + 0.5
        return tiscon_c

    def abc_method(self):
        return 'abstract check in coat'

class Suit(Dress):

    @property
    def suit_f(self):
        tiscon_s = 2 * self.V + 0.3
        return tiscon_s

    def abc_method(self):
        return 'abstract check in suit'


c_class = Coat(13)
print(c_class.coat_f)

s_class = Suit(0)
print(s_class.suit_f)

print(c_class.coat_f + s_class.suit_f)

print(c_class.abc_method())
print(s_class.abc_method())