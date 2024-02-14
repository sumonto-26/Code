a = list(map(int,input().split(" "))) 
b = list(map(int,input().split(" ")))
n = 0

for i in range(a[0]):
    if a[1] >= b[i]:    n += 1
    else:   n += 2

print(n) 
