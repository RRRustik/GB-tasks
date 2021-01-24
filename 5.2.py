"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open("task2", "r")


count_l = 0
for line in file:
    count_l +=1

    words = line.split()
    count_w = len(words)

    print(f'В строке №{count_l} всего {count_w} слова')
print(f'Всего количество строк {count_l}')


file.close()