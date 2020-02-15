n, m, k = (int(i) for i in input().split()) # строки, столбцы, кол-во мин

a = [[0 for j in range(m)] for i in range(n)] # пустая таблица из 0
for i in range(k): # перебираем кол-во мин
    row, col = (int(i) - 1 for i in input().split()) # записываем строку и столбец одной мины при каждом проходе
    a[row][col] = -1 # записываем мину по координатам строки и столбца

'''проверка наличия мин в клетках, соседних с текущей клеткой, не содержащей мин. 
Если в соседней клетке есть мина, увеличиваем на 1 счетчик в текущей клетке'''

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1

# Вывод клеток с минами и остальных клеток таблицы

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='\t')
        elif a[i][j] == 0:
            print('.', end='\t')
        else:
            print(a[i][j], end='\t')
    print()