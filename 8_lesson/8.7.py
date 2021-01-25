"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""




class Complex_num:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return f' {self.x + other.x} + {(self.y + other.y)} * i '

    def __mul__(self, other):
        return f' {self.x * other.x - self.y * other.y} + {self.x * other.y + self.y * other.x} * i'


compl_x = Complex_num(1, 2)
compl_y = Complex_num(1, 1)

print(compl_x.__add__(compl_y))
print(compl_x.__mul__(compl_y))
