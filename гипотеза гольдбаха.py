n = int(input())
u = 0
i = 2
while i < n and u == 0:
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c += 1
    if c == 0:
        m = n - i
        p = 0
        for j in range(2, m):
            if m % j == 0:
                p += 1
        if p == 0 and m != 1:
            print(i, m)
            u += 1
    i += 1
