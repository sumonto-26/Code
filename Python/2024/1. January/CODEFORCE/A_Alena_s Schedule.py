n = int (input())
a = list(map(int, input().split(" ")))
c=0
if 1 in a:
    s = a.index(1)
    for i in range(s, n-1):
        c+=1
        if a[i]==0 and a[i+1] ==0:
            break
        if i==n-2:
            c+=1
        
    print(c)
else:
    print(c)