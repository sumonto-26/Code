a = sorted(map(int, input().split(" ")))
s = sum(a) / 2

a3 = []

for i in range(1, len(a)):
    a1 = a[0] + a[i]
    a2 = int(s - a1)

    if a2 in a[i+1:]:
        a3 = [a[0], a[i], a2]
        break

for j in a3:
    a.remove(j)

if sum(a3) == sum(a):
    print("YES")
else:
    print("NO")