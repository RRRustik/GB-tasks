#name = input("Введите название товара: ")
#price = int(input("Введите цену товара: "))
#amount = int(input("Введите количество товара: "))
"""
q = int(input("Введите кол-во товаров: "))

dict1 = dict()
list1 = list()
for i in range(q):
    name = input(f'Введите название товара №{i+1}: ')
    price = int(input("Введите цену товара: "))
   # amount = int(input("Введите количество товара: "))
   # measure = input("Введите единицу измерения: ")
    dict1["Название"] = name
    dict1["Цена"] = price
   # dict1["Количество товара"] = amount
   # dict1["Единица измерения"] = measure
   # for k in range(q):
    list1.append(i+1)
    list1.append(dict1)
    tuple1 = tuple(list1)
    print(tuple1)
"""
  #  if len(var) >= 10:
    #    print(index+1, var[:])

goods = []
while input("Would you like add product? Enter yes/no: ") == 'yes':
    number = int(input("Enter product number: "))
    features = {}
    while input("Would you like add product parameters? Enter yes/no: ") == 'yes':
        feature_key = input("Enter feature product: ")
        feature_value = input("Enter feature value product: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)

#5
"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
num = input("Введите строку из чисел, разделенных пробелами: ")

def sum_func(num):
    b = num.split()
    sum_num = 0
    for index, var in enumerate(b):
        sum_num += num[index]
    return sum_num


print(sum_func(num))



