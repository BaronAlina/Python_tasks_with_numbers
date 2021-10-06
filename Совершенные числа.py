n=int(input())
s=[]
i=1
b=0
while i<n:
    if(n%i==0):
        b+=i
        s.append(i)
    i+=1
if(b==n):
    print(*s, end=' ')
else:
    print(0)
