def magic_square(n):
    num = (n * ((n * n) + 1)) / 2
    print('\nThe Magic Number Is:-', num, '\n')
    f = []
    for i in range(0, n):
        a = []
        for j in range(0, n):
            a.append(0)
        f.append(a)
    (x, i, p, q) = (n * n, 1, int(n / 2), n - 1)
    while x != 0:
        if x == 0:
            (f[p][q], i, p, q, x) = (i, i + 1, p - 1, q + 1, x - 1)
            continue
        else:
            if p == -1 and q == n:
                p = 0
                q = n - 2
                if f[p][q] == 0:
                    (f[p][q], i, p, q, x) = (i, i + 1, p - 1, q + 1, x - 1)
                    continue
                else:
                    p = p + 1
                    q = q - 2
                    f[p][q] = i
                    i = i + 1
                    p = p - 1
                    q = q + 1
                    x = x - 1
                    continue
            if p == -1:
                p = n - 1
                if f[p][q] == 0:
                    (f[p][q], i, p, q, x) = (i, i + 1, p - 1, q + 1, x - 1)
                    continue
                else:
                    p = p + 1
                    q = q - 2
                    f[p][q] = i
                    i = i + 1
                    p = p - 1
                    q = q + 1
                    x = x - 1
                    continue
            if q == n:
                q = 0
                if f[p][q] == 0:
                    (f[p][q], i, p, q, x) = (i, i + 1, p - 1, q + 1, x - 1)
                    continue
                else:
                    p = p + 1
                    q = q - 2
                    f[p][q] = i
                    i = i + 1
                    p = p - 1
                    q = q + 1
                    x = x - 1
                    continue
            else:
                if f[p][q] == 0:
                    (f[p][q], i, p, q, x) = (i, i + 1, p - 1, q + 1, x - 1)
                    continue
                else:
                    p = p + 1
                    q = q - 2
                    f[p][q] = i
                    i = i + 1
                    p = p - 1
                    q = q + 1
                    x = x - 1
                    continue
    for i in range(len(f)):
        for j in range(len(f[i])):
            print(f[i][j], end="   ")
        print("\n")

magic_square(4)