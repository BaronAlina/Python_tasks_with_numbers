n = int(input())
u = 0
for k in range(2, n + 1):
    c = 0
    for i in range(2, k):
        if k % i == 0:
            c += 1
    if c == 0 and n % k == 0:
        m = 0
        r = n
        while r % k == 0 and r != 0:
            m += 1
            r = r // k
        if m == 1:
            if u != 0:
                print('*', end = '')
            u = u + 1
            print(k, end = '')
        else:
            if u != 0:
                print('*', end = '')
            u = u + 1
            print(k, '^', m, sep = '', end = '')
