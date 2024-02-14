# 17 January 2023
ans = 0
l = list(map(int, input().split(" ")))

for i in range(1, l[0] + 1):
    if l[1] % i == 0 and l[1] // i <= l[0]:
        ans += 1

print(ans)
