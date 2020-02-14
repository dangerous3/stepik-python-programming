a = [int(i) for i in input().split()]

already = False
res = []
i = 0

a.sort()

if len(a) == 1:
    print()
else:
    while i <= len(a) - 1:
        if i == len(a) - 1:
            if a[-1] == a[-2] and already == False:
                break
            else:
                if already == True:
                    res.append(a[i])
                break
        if a[i] == a[i + 1]:
            i += 1
            already = True
            continue
        else:
            if already == True:
                res.append(a[i])
                already = False
            i += 1

    print(*res)