a,b = map(int,input().split(" "))
ans = -1
for i in range(a,b+1):
    if len(set(list(str(i)))) == len(str(i)):
        ans = i
        break
        
print(ans)