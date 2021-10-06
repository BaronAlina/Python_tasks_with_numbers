a = int(input())
b = 1
for i in range(1, a // 2 + 1):
    n, m = i, a - i
    while n != 0 and m != 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    if n == 1 or m == 1:
        b = i
print(b, a - b)
