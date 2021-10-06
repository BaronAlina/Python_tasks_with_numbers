k = int(input())
for n in range(1, k + 1):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s+=i
    for m in range(1, n + 1):
        if s == m and m != n:
            p = 0
            for i in range(1, m):
                if m % i == 0:
                    p = p + i
            if p == n:
                if m > n:
                    print(n, m)
                else:
                    print(m, n)
