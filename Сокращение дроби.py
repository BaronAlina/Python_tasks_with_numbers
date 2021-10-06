a, b= map(int, input().split())
a1=a
b1=b
if a<0 or b<0:
    while a!=b:
        if a<b:
            a=a+b
        else:
            b=b+a
else:
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
print(int(a1/a), end=' ')
print(int(b1/a))
