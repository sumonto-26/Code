# Date --> 15 December 2023 
# //////my logic/////
# submit at 12:11 AM accepted in first try

a = int (input())
for i in range(a):
    b = list(map(int,input().split(" ")))
    c = sorted(b)
    d = (c[1] + c[2])
    if d >= 10:
        print("YES")
    else:
        print("NO")