n,m = map(int, input().split(" "))
f = sorted(map(int, input().split(" "))) 
l = []
for i in range(m-n+1):
    arr = f[i:i+n]
    l.append(max(arr)-min(arr))
    
ans = min(l)
print(ans)