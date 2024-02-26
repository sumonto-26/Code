# Date ==> 26 February 2024

for _ in range(int(input())):
    a = list(map(int,input().split()))
    
    ans = (a[1]-1) // (a[0]-1)
    print(ans + a[1])