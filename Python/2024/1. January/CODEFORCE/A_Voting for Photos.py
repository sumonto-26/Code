n = int(input())
a = list(map(int, input().split(" ")))

# l = list(set(a))
ab = []
for i in range(n):
    c = a.count(a[i])
    ab.append(c)

m = max(ab)

last_idx = []
for i in  ab:
    c = 0
    for j in range(n):
        if l[i]==a[j]:
            c+=1
            if c==m:
                last_idx.append(j)

ans = min(last_idx)
# print(last_idx)
# print(ans)
print(a[ans], l , last_idx, ans)

