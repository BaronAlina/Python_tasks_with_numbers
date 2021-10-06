a,b,c,d=map(int, input().split())
m=a*d+b*c
n=d*b
c=m
d=n
while m != 0 and n != 0:
    if m > n:
        m = m % n
    else:
        n = n % m
if m != 0:
    print(c// m, d// m)
else:
    print(c// n, d// n)
