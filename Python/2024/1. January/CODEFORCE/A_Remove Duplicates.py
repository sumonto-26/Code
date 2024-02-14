# Date 19 January 2024

n = int(input())
a = list(map(str,input().split(" ")))
l = []

for i in range(n-1, -1, -1):
    if a[i] in l :
        pass
    else:
        l.append(a[i])

print(len(l))
ans = list(reversed(l))
answer = ' '.join(ans)
print(answer)