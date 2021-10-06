a, b= map(int, input().split())
if a<0 and b<0:
    a=-a
    b=-b
a1=a
for i in range(1, a1+1):
    if a%i==0 and b%i==0:
        a=a//i
        b=b//i
print(a, b, end=' ')
