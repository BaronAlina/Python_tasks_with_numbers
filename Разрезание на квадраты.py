a, b = map(int, input().split())
if b > a: a, b = b, a
if a % b == 0:
    print(a // b)
else:
    count = 0
    while a % b != 0:
        count += a // b
        a, b = b, (a % b)
    if a % b == 0:
        count += a // b
    print(count)
