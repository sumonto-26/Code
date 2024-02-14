a = int(input())
b = list(map(int,input().split(" ")))
m = 1
c = 1
for i in range(a-1):
    if b[i] <= b[i+1]:
        c += 1
    else:
        m = max(m , c)
        c = 1
m = max(m,c)
print(m)
