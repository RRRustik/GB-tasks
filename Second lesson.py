#1
"""
s = [2, 3.0, "Dva", None]
m = len(s)
for i in range(m):
    print(type(s[i]))
"""


#2
"""
sp = []
n = int(input("Введите кол-во элементов списка: "))
for i in range(n):
    t = int(input(f' {i+1}-й элемент списка: '))
    sp.append(t)
#k = int(len(sp)/2)
for j in range(0, len(sp), 2):
    sp[j], sp[j+1] = sp[j+1], sp[j]
print(len(sp))
print(sp)
"""



#3
"""
z = int(input('Введите номер месяца: '))
#season_dict = {'1': 'Зима', '2': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето', '7': 'Лето', '8': 'Лето', '9': 'Осень', '10': 'Осень', '11': 'Осень', '12': 'Зима'}
season_dict1 = dict()
for i in range(12): #Более умного подхода к заполнению месяцев не нашел
    i+=1
    if i <=2 or i == 12:
        season_dict1[i] = 'Зима'
    elif 3 <= i <= 5:
        season_dict1[i] = 'Весна'
    elif 6 <= i <= 8:
        season_dict1[i] = 'Лето'
    else:
        season_dict1[i] = 'Осень'
print(season_dict1)
print(season_dict1.get(z))


season_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
p = int(z)
print(season_list[p-1])
"""



#4
"""
words = str(input('Введите несколько слов через пробел: '))
b = words.split()
for index, var in enumerate(b):
    print(index+1, var[0:10])

"""



#5
"""
set_numbers = [23, 21, 18, 14, 9, 5]
new_set = []
l = int(input('Введите новый элемент рейтинга: '))
i = 0
for i in range(len(set_numbers)):
    if l <= set_numbers[i]:
        new_set.append(set_numbers[i])
        k = i+1
    else:
        new_set.append(set_numbers[i])
new_set.insert(k, l)
print(new_set)
"""
#6
q = int(input("Введите кол-во товаров: "))

goods = []
dict1 = {}
i = 0
while i < q: #Не понимаю почему он в словаре каждый раз перезаписывает данные по продуктам
    name = input(f'Введите название товара №{i+1}: ')
    price = int(input("Введите цену товара: "))
    amount = int(input("Введите количество товара: "))
    measure = input("Введите единицу измерения: ")
    dict1["Название"] = name
    dict1["Цена"] = price
    dict1["Количество товара"] = amount
    dict1["Единица измерения"] = measure
    from copy import deepcopy
    dict2 = deepcopy(dict1)
    goods.append(tuple([i+1, dict2]))
    i += 1
print(goods)

dict2 = dict()
for n in goods:
    for feature_key, feature_value in n[1].items():
        if feature_key in dict2:
            dict2[feature_key].append(feature_value)
        else:
            dict2[feature_key] = [feature_value]
print(dict2)
