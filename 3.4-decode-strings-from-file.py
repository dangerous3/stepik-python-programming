'''На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление
исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка
"download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас
получится, надо отправить в качестве ответа на эту задачу.
'''


def decode_strings(item):
    s = ''
    result = ''
    i = 0
    tempnum = ''
    length = len(item) - 1
    while i <= (len(item) - 1):
        if item[i].isalpha():
            s = item[i]
            i += 1
        else:
            while item[i].isdigit() and i < (len(item) - 1):
                tempnum = str(tempnum) + str(item[i])
                i += 1
            if i == len(item) - 1:
                tempnum = str(item[i])
                s = s * int(tempnum)
                result = result + s
                return(result)
            s = s * int(tempnum)
            result = result + s
            tempnum = ''

# Строка для отладки
#a = 'A3b4c2E10b1'
#print(decode_strings(a))

# Для отладки используйте файл ./samples/decode-this-example.txt. Результат выведен в файле ./samples/decode-result.txt
with open('/home/dangerous3/Загрузки/dataset_3363_2(1).txt', 'r') as dec, open('/home/dangerous3/Загрузки/dataset_3363_2-decoded.txt', 'w') as wr:
    for line in dec:
       line = line.strip()
       wr.write(decode_strings(line) + "\n")



