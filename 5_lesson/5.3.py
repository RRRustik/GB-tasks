"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
file = open('task3', 'r')

common_salary = 0
count = 0

for line in file:
    line = line.split()
    salary = int(line[1])
    count += 1
    common_salary += salary

    if salary < 20000:
        print(f' Зарплата сотрудника {line[0]} составляет {line[1]}')

av_salary = common_salary/count
print(f' Средняя зарплата сотрудника составляет {av_salary}')

file.close()