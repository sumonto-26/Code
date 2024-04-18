import math
n,m,a,b = map(int,input().split())
ans = [n*a]
if n <= m:
    ans.append(b)
else:
    ans.append(math.ceil((n/m))*b)
    ans.append(math.floor((n//m)*b) + (a*(n%m)))
    
print(min(ans))