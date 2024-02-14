from math import sqrt

n = int(input())
for _ in range(n):
    a = int(input())
    b = list(map(int, input().split()))
    ans = sqrt(sum(b))
    if ans == int(ans):
        print("YES")
    else:
        print("NO")