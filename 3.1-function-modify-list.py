'''Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
 а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка'''

def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 != 0:
            del l[i]
        else:
            l[i] = l[i] // 2

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst)) # None
print(lst)              # [1, 2, 3]
modify_list(lst)
print(lst)              # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]