a = list(map(int,input().split(" ")))
b = sorted(map(int,input().split(" ")))
n = []
for i in range(a[1]):
    if b[i] <= 0:
        n.append(b[i])
ans = sum(n) * -1
print(ans)