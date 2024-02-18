import math 
def solve(a,n):
    m = 1
    l = a
    ans = 0
    while ans < n:
        m += 1
        for i in a:
            i == i * m
            if math.lcm(a) == math.lcm(l):
                pass
            else:
                ans += 1
    return m

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if a == sorted(a):
        print(n)
    else:
        ans  = solve(a, n)
        print(ans)
        