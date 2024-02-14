n = int (input())
e=0
for i in range(n):
    a = int (input())
    b = int (input())
    c = int (input())
    d = a+b+c
    if d>1:
        e+=1
print(e)