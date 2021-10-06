n = int(input())
a = 1
for i in map(int, input().split()):
    b = i
    if a == 1:
        a = i
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
print(a)
