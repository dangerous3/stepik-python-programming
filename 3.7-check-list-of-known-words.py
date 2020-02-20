'''Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d d d известных нам слов, после чего на d d d строках указываются
 эти слова. Затем передаётся количество l l l строк текста для проверки, после чего l l l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the
'''

n = int(input())
known_words = []
checked_words = []
errors = {}

for i in range(n):
    vocab = str(input()).lower()
    known_words.append(vocab)

k = int(input())

for j in range(k):
    checked = input().split()
    checked_words.append(checked)

checked_words = [w.lower() for line in checked_words for w in line]

for j in checked_words:
    if j not in known_words:
        errors[j] = 'Unknown word'

for error in errors.keys():
    print(error)

