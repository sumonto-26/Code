# DATE ==> 25 June 2024
# AUTHOR ==> SUMONTO
for _ in range(int(input())):
    n = int(input())
    a, b = 1, int(n**(1/3))+1
    while(a<=b):
        s = (a**3)+(b**3)
        if a == int(a) and b == int(b) and s == n:
            print("YES")
            break
        elif s>n:
            b -= 1
        elif s<n:
            a+= 1
    else:
        print("NO")
            

