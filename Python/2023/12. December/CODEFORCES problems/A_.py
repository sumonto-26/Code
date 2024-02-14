# Date 31 December 2023

for i in range(int(input())):
    a = list(map(int,input().split(" ")))
    if a[0] == 0:
        print("1")
    else:
        an = a[1]*2
        ans = an + a[0]
        print(ans+1)


