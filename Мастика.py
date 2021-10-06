a, b, c, N = map(int, input().split())
count = 0
for i in range(0, int(N/a) + 1):
    for j in range(0, int(N/b) + 1):
        r=N-(i*a+j*b)
        if r >= 0 and r % c == 0:
            count = count + 1
print(count)
for i in range(0, int(N/a) + 1):
    for j in range(0, int(N/b) + 1):
        r=N-(i*a+j*b)
        if r >= 0 and r % c == 0:
            print(i,j,r//c)
