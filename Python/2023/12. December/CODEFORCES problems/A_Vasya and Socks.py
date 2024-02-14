a = list(map(int, input().split(" ")))


s = a[0] # n
ans = 0
i = 1
while i<=s: 
    ans += 1
    if (i % a[1] == 0):
        s += 1
    i +=1
   
print(ans)

