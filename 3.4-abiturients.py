'''Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его
среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике,
физике и русскому языку по всем абитуриентам.

В качестве ответа на задание прикрепите полученный файл со средними оценками.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']'''


table =[]

# Данные для отладки: './samples/abitur.txt'

with open('/home/dangerous3/Загрузки/dataset_3363_4.txt', 'r') as abi:
    for line in abi:
        line = line.strip()
        #temp = line.split(';')
        table.append(line)


for i in range(len(table)):
    table[i] = table[i].split(';')

#print(table)


math_sum = 0
phys_sum =0
rus_sum = 0

with open('/home/dangerous3/Загрузки/dataset_3363_4-decoded.txt', 'w') as wr:
    all_av = ''
    for surname in range(len(table)):
        average = list(map(float, table[surname][1:]))
        average = str(round(sum(average) / 3, 9))
        wr.write(average + "\n")
        math_sum += float(table[surname][1])
        phys_sum += float(table[surname][2])
        rus_sum += float(table[surname][3])
    wr.write(str(round(math_sum / 3, 9)) + " " + str(round(phys_sum / 3, 9)) + " " + str(round(rus_sum / 3, 9)))

