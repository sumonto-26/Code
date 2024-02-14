a = int(input())
b = input()
n = []
m = []
for i in range(a-1):
    k = b[i]+b[i+1]
    n.append(k)
    l = n.count(k)

    m.append(l)
    index = m.index(max(m))

print(n[index])