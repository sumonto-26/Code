l = int(input())
a = sorted(map(int, input().split(" "))) 
h = []
for i in range(0,len(a)):
    n = a.count(a[i])
    h.append(n)
m = max(h)
w = set(a)
print(m, len(w))
