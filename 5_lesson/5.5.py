"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

sum_list = []
with open("task5.txt", "w") as f_obj:
    numbers = input('Введите числа через пробел: ')

    f_obj.write(numbers)
    num = numbers.split()
    print(numbers)

    for i in range(len(num)):
        sum_list.append(int(num[i]))

total = sum(sum_list)
print(total)