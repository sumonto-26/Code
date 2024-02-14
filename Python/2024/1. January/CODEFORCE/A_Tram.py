# Date --> 17 January 2024

n = []
s = []
ans = 0
for _ in range(int(input())):
    a = list(map(int, input().split(" ")))
    n.append(a)

for i in n:
    ans -= i[0] 
    ans += i[1] 
    s.append(ans)

print(max(s))