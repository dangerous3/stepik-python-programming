'''Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.'''

import requests
import os

url = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('/home/dangerous3/Загрузки/dataset_3378_3.txt', 'r') as urlfile:
    for line in urlfile:
        line = line.strip()
        if line.find('We') == -1:
            r = requests.get(line)
            line = r.text
        while line.find('We') == -1:
            newurl = os.path.join(url, line)
            r = requests.get(newurl)
            line = r.text
print(line)
