l = list(map(int,input().split(" ")))
n = list(map(int,input().split(" ")))
k = n[0]
m = n[1]

a = sorted(map(int,input().split(" ")))
b = reversed(sorted(map(int,input().split(" "))))
a = a[ : k]
b = list(b)[ : m]

ans = "YES"
for i in a:
    for j in b:
        if i >= j:
            ans = "NO"
            break
            
print(ans)
        
        
        
# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE