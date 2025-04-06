# Author ===> SUMONTO
# DATE ===> 6/April/2025

def solve(x1,p1,x2,p2):
    x1,x2 = str(x1), str(x2)
    cx1,cx2 = x1,x2
    if len(x1) < len(x2) : x1 = x1 + '0'*min(p1, len(x2) - len(x1))       
    elif len(x1) > len(x2) : x2 = x2 + '0'*min(p2, len(x1) - len(x2))
    x1 = int(x1)
    x2 = int(x2)
    p1 = min(p1,p1-min(p1, len(cx2) - len(cx1)))
    p2 =  min(p2, p2-min(p2, len(cx1) - len(cx2)))
    # print(x1,p1 , "\n",x2,p2)
    
    if(p1 > p2): return '>'
    elif (p1 < p2): return '<'
    elif x1 == x2 and p1 == p2: return '='
    else: 
        if x1 > x2: return '>'
        else: return '<' 
    
            

for _ in range(int(input())):
    x1,p1 = list(map(int,input().split()))
    x2,p2 = list(map(int,input().split()))
    print(solve(x1,p1,x2,p2))