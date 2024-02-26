# Date ==> 26 February 2024
n = int(input())
a = list(map(int,input().split(" ")))

ans = 0
e = 0
o = 0
for i in range(n):
    if a[i] % 2 == 0 :
        e += 1
    else:
        o += 1
        
for j in range(n):
    if e == 1:
        if a[j] % 2 == 0:
            print(j+1)
    else:
        if a[j] % 2 != 0:
            print(j+1)