# DATE ==> 26 JUNE 2024
# AUTHOR ==> SUMONTO

for _ in range(int(input())):
    a,b,x,y,n = map(int,input().split())
    
    if n >= (a+b)-(x+y): print(x*y)
    if a >= b:
        if n <= (b-y):
            print(a*(b-n))
        else:
            a -= n-(b-y)
            b = y
            print(a*b)
    else:
        if n <= (a-x):
            print(b*(a-n))
        else:
            b -= n-(b-y)
            b = y
            print(a*a)
        