def solve(a,b):
    if(a==b):
        if(a%2 == 0): return a
        else: return -a
    else:
        if (a%2 == 0):
            if b%2 == 0: return (((b-a)+1)/2)+a
            else : return (((b-a)+1)/2)*-1
        else:
            if b%2 == 0: return ((b-a)+1)//2
            else: return (((b-a)+1)//2)-b
    
for _ in range(int(input())):
    l,r = map(int,input().split())
    d = (r-l)+1
    ans = int(solve(l,r))
    print(ans)