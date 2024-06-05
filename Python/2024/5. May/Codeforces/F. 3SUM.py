# DATE ==> 12 May 2024
# AUTHOR ==> SUMONTO 

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    a = [i%10 for i in arr]
    d = list(set(a))
    for i in range(len(set(a))):
        if a.count(d[i]) >= 3:
            d.append(d[i])
            d.append(d[i])
        if len(d) == 30: break

    n = len(d)
    ans = False
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                if (d[a]+d[b]+d[c])%10 == 3 and a!=b and a!=c and b!=c:
                    ans = True
                    break
            if ans: break
        if ans: break
    print("YES" if ans else "NO")

