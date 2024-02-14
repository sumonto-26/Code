nk = list(map(int,input().split(" ")))
a = list(map(int,input().split(" ")))
l = []
n = 0
for i in range(nk[0]):
    if a[i-1] != a[i]:
        n += 1
        l.append(n)
    else:
        n = 1
        l.append(n)
print(max(l))