'''Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две
строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного
алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно
расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac'''

input_str = str(input())
cypher = str(input())
need_to_encode = str(input())
need_to_decode = str(input())

temp_input = []
temp_cypher = []
res_dict = {}
result_encode = ''
result_decode = ''

for i in input_str:
    temp_input.append(i)

for j in cypher:
    temp_cypher.append(j)

for i in range(len(input_str)):
    res_dict[input_str[i]] = temp_cypher[i]

for j in need_to_encode:
    result_encode = result_encode + res_dict[j]
print(result_encode)

for j in need_to_decode:
    result_decode = result_decode + str(list(res_dict.keys())[list(res_dict.values()).index(j)])
print(result_decode)
