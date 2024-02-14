# Date ==> 18 January 2024

l = int(input())
a = list(map(int,input().split(" ")))
b = 1
m = min(a)
n = []
e = []

index = a.index(m)
for i in range(l):
    if a[i] == m:
        n.append(i)

for j in range(len(n)-1):
    ans = n[j+1] - n[j]
    e.append(ans) 

print(min(e))