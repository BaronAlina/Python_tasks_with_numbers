n = int(input())
i = 2
if n % i :
    for i in range(3, n + 1, 2) :
        if not n%i:
            break
print(n//i, (i-1)*(n//i))
