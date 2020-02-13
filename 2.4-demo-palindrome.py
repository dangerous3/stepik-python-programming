'''Проверка, является ли введенная строка палиндромом'''

s = input()
i = 0
j = len(s) - 1
is_palindrom = True
while i < j:
    if s[i] != s[j]:
        is_palindrom = False
        break
    i += 1
    j -= 1
if is_palindrom:
    print('YES')
else:
    print('NO')

 # Alternative version^
'''s = input()
r = s[::-1]
if s == r:
    print('YES')
else:
    print('NO')'''