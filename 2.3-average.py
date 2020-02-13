a = int(input())
b = int(input())
s = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        count += 1
        s += i
if s == 0:
    print("Внутри интервала нет целых значений, делящихся на 3")
else:
    print(s / count)
