"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""



#print(file.read())

dict_en_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

dict_file_new = []

file = open('task4', 'r')

for line in file:
    line = line.split(' ', 1)
    dict_file_new.append(dict_en_ru[line[0]] + ' ' + line[1])
print(dict_file_new)



file_new = open('file4.txt', 'w')
file_new.writelines(dict_file_new)

file.close()
file_new.close()
    #for word in range(len(line)):
    #file_new.write(line)
        #w = word[0]
       # print(w)





#f = [line.strip() for line in file]
#for line1 in file_new:
    #file_new.write(line1 + '\n')


