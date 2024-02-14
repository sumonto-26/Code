# date 3 december 2023
a, b = map(int,input().split())
c = list(map(int,input().split()))
n = 0
for i in range(0, a):
    if c[i] >= c[b-1] and c[i] >= 1:
        n += 1
print(n)