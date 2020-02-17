'''Выведите таблицу размером n×n n \times n n×n, заполненную числами от 1 1 1 до n2 n^2 n2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5 n=5 n=5):

Sample Input:

5

Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9'''

n = int(input())

a = 0
b = 0

ai = 0
bi = 1

# Заполняем матрицу нулями
mat = [[0 for j in range(n)] for i in range(n)]

# Обход матрицы по часовой стрелке
for i in range(1, n ** 2 + 1):
    mat[a][b] = i
    ax = a + ai
    by = b + bi
    if 0 <= ax < n and 0 <= by < n and not mat[ax][by]:
        a = ax
        b = by
    # Если выходим за пределы матрицы, или значение заполняемой ячейки не равно 0, то поворачиваем вниз или влево
    else:
        temp = bi
        # Поворот
        bi = -ai
        ai = temp
        a = a + ai
        b = b + bi

for i in range(len(mat)):
    print(*mat[i], end='\t')
    print()
