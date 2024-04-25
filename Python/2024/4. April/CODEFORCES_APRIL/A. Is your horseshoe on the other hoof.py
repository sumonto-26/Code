a = list(map(int,input().split()))
s = list(set(a))

ans = []
for i in range(len(s)):
    c = a.count(s[i])
    ans.append(c-1)
    
print(sum(ans))