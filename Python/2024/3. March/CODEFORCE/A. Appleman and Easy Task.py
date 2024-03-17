ans = "NO"
l = []
c = []
n = int(input())
for _ in range(n):
    a = list(map(str, input()))
    c.append(str(a.count("o")))
    
    if "o" in a:
        l.append(a.index("o"))
        if len(set(a)) == 1:
            ans = "YES"
            break
        
if len(set(l)) == 1 and "0" not in c or\
    len(set(l)) == n and l == sorted(l) and min(c) != 0 or\
    len(set(l)) == n and list(reversed(sorted(l))) == l and min(c) != 0 :
    ans = "YES"

print(ans)
        