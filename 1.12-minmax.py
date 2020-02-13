'''Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.'''

a = int(input())
b = int(input())
c = int(input())

max_num = max(a, b, c)
min_num = min(a, b, c)

if max_num == a and min_num == b or max_num == b and min_num == a:
    third = c
elif max_num == a and min_num == c or max_num == c and min_num == a:
    third = b
elif max_num == b and min_num == c or max_num == c and min_num == b:
    third = a

print(max_num)
print(min_num)
print(third)