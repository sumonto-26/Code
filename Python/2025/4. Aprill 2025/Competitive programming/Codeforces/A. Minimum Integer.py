for _ in range(int(input())):
    l,r,d = map(int,input().split())
    if(d<l or d>r): print(d)
    else:
        if(r%d == 0): print(r+d) 
        else: print(r-(r%d)+d)       
         